import http.server
import socketserver
import json
import os
import threading

PORT = int(os.environ.get("PORT", 5000))
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "montreal_state.json")
lock = threading.Lock()

def load_state():
    with lock:
        if not os.path.exists(DATA_FILE):
            return {}
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading state: {e}")
            return {}

def save_state(state):
    with lock:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        tmp_file = DATA_FILE + ".tmp"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
        os.replace(tmp_file, DATA_FILE)

class MontrealTripHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def send_json(self, data, status=200):
        response_bytes = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

    def do_GET(self):
        if self.path == "/api/state":
            state = load_state()
            safe_state = dict(state)
            safe_state.pop("admin_pin", None)
            return self.send_json(safe_state)
        super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_length).decode("utf-8")
        try:
            payload = json.loads(post_body) if post_body else {}
        except Exception:
            return self.send_json({"error": "Invalid JSON"}, 400)

        state = load_state()

        if self.path == "/api/arrival":
            member_id = payload.get("member_id")
            if not member_id:
                return self.send_json({"error": "Missing member_id"}, 400)
            
            if "arrivals" not in state:
                state["arrivals"] = {}
            
            state["arrivals"][member_id] = {
                "date": payload.get("date", "Thu Oct 8"),
                "time": payload.get("time", ""),
                "flight": payload.get("flight", ""),
                "notes": payload.get("notes", "")
            }
            save_state(state)
            safe_state = dict(state)
            safe_state.pop("admin_pin", None)
            return self.send_json(safe_state)

        elif self.path == "/api/vote":
            member_id = payload.get("member_id")
            item_id = payload.get("item_id")
            vote_type = payload.get("vote") # 'up', 'down', 'none'
            
            if not member_id or not item_id or vote_type not in ("up", "down", "none"):
                return self.send_json({"error": "Invalid vote parameters"}, 400)
            
            if "votes" not in state:
                state["votes"] = {}
            if item_id not in state["votes"]:
                state["votes"][item_id] = {"up": [], "down": []}
            
            # Remove member from both up and down first
            if member_id in state["votes"][item_id].get("up", []):
                state["votes"][item_id]["up"].remove(member_id)
            if member_id in state["votes"][item_id].get("down", []):
                state["votes"][item_id]["down"].remove(member_id)
            
            if vote_type == "up":
                state["votes"][item_id]["up"].append(member_id)
            elif vote_type == "down":
                state["votes"][item_id]["down"].append(member_id)

            save_state(state)
            safe_state = dict(state)
            safe_state.pop("admin_pin", None)
            return self.send_json(safe_state)

        elif self.path == "/api/coffee":
            shop_id = payload.get("shop_id")
            level = payload.get("level")
            if not shop_id or level not in (0, 1, 2):
                return self.send_json({"error": "Invalid coffee parameters"}, 400)
            
            if "coffee_prefs" not in state:
                state["coffee_prefs"] = {}
            state["coffee_prefs"][shop_id] = level
            save_state(state)
            safe_state = dict(state)
            safe_state.pop("admin_pin", None)
            return self.send_json(safe_state)

        elif self.path == "/api/admin/schedule":
            pin = str(payload.get("pin", ""))
            stored_pin = str(os.environ.get("ADMIN_PIN", state.get("admin_pin", "2026")))
            if pin != stored_pin:
                return self.send_json({"error": "Invalid PIN"}, 403)
            
            new_schedule = payload.get("schedule")
            if new_schedule and isinstance(new_schedule, list):
                state["schedule"] = new_schedule
                save_state(state)
                safe_state = dict(state)
                safe_state.pop("admin_pin", None)
                return self.send_json(safe_state)
            else:
                return self.send_json({"error": "Invalid schedule data"}, 400)

        elif self.path == "/api/admin/verify":
            pin = str(payload.get("pin", ""))
            stored_pin = str(os.environ.get("ADMIN_PIN", state.get("admin_pin", "2026")))
            if pin == stored_pin:
                return self.send_json({"success": True})
            return self.send_json({"error": "Invalid PIN"}, 403)

        return self.send_json({"error": "Endpoint not found"}, 404)

    def log_message(self, format, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True

def run_server():
    global PORT
    ports_to_try = [PORT, 5050, 8000, 8080]
    for p in ports_to_try:
        try:
            httpd = socketserver.TCPServer(("0.0.0.0", p), MontrealTripHandler)
            print(f"Starting Montreal Trip Server on port {p}...")
            httpd.serve_forever()
            break
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"Port {p} in use, trying next port...")
                continue
            raise

if __name__ == "__main__":
    run_server()
