# Montreal 2026: Family Trip Planning & Live Coordination Hub

An interactive, live-state web app for the Montreal Canadian Thanksgiving long weekend trip (October 8–12, 2026, 11 guests at 3831 Boulevard Saint-Laurent in the Plateau).

## Features

- **Live Multi-User Sync:** Backed by Python REST API in `server.py` and persistent JSON store in `data/montreal_state.json`.
- **Zero-Friction Identity Switcher:** Family members choose their name from the top bar to vote and record arrivals without passwords.
- **L'Arrivée (Arrivals Board):** Interactive Thursday touchdown and flight tracker with confirmed landing times for Michael, Haley, Dani & Travis, and driving convoy details for Greg, Cat, Owen, Izzy & Michele.
- **Le Plan Live (Concierge Schedule):** Live 5-day schedule featuring confirmed reservations, active polls, and Michael's PIN-protected Admin edit drawer (`Default PIN: 2026` or configured via `ADMIN_PIN` env var).
- **La Table (Marquee Dinners for 11):** Up/down voting on Schwartz's, Le Serpent, Monarque, Au Pied de Cochon, Damas, and L'Express with voter tallies and dual Google & Yelp ratings.
- **Le Café & La Pâtisserie (30-Min Doorstep Walk Radius):** 12 curated specialty single-origin roasters and French bakeries with side-by-side Google and Yelp reviews, signature items, and Haley's Coffee Desire Tracker.
- **Alan's Discovery Guide & Traz Commentary:** Custom animated stickers of Traz with tactical notes across Breakfast & Bagels, Poutine & Casual, Desserts & Pastries, Bars & Nightlife, and Attractions with live group upvoting.
- **Conseils & Practical Tips:** Bank of America/Scotiabank free ATMs, parking/street cleaning signs in French, transit, and Airbnb lock dates.

## Project Structure

- `index.html` (and `montreal.html`) — Main Montreal interactive web app
- `server.py` — Python HTTP & REST API server (`/api/state`, `/api/arrival`, `/api/vote`, `/api/coffee`, `/api/admin/schedule`, `/api/admin/verify`)
- `data/montreal_state.json` — Persistent atomic store for votes, flight arrivals, and schedule
- `assets/` — Custom Pop! hero illustration, map assets, and Traz character stickers

## Running the App

```bash
python3 server.py
```

Runs on port `5000` (on Replit) or automatically falls back to `5050` / `8000` locally.
