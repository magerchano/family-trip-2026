# DESIGN.md — Montréal 2026 Family Trip Web App

## 1. Product Overview & Context
- **Product Name:** Montréal 2026 Travel & Concierge App
- **Trip Dates:** October 8–12, 2026 (Canadian Thanksgiving Long Weekend)
- **Basecamp Location:** 3831 Boulevard Saint-Laurent, The Plateau, Montreal, QC (Historic brownstone with 2 rooftop terraces)
- **Headcount:** 11 Guests (9 Adults + Owen, 12 and Izzy, 10)
- **Core Purpose:** An elevated, editorial, live-collaborative family vacation site that coordinates arrivals, collects real-time up/down votes on group dinners and activities, presents a curated walkable coffee & bakery guide, and displays a live concierge itinerary with admin controls.

---

## 2. Visual Identity & Design System

### 2.1 Aesthetic Theme: "Autumn on The Main"
- **Mood:** French-Canadian bistro elegance meets warm Autumn in the Plateau. Bespoke, editorial, magazine-grade layout with intimate family warmth.
- **Visual References:** *Condé Nast Traveler*, *Monocle City Guides*, classic French brasserie menus, and vintage Montreal illustrated maps.

### 2.2 Color Palette (Tokens)
```css
:root {
  /* Backgrounds & Surfaces */
  --color-bg: #faf8f5;                /* Warm French limestone cream */
  --color-surface: #faf8f5;           /* Primary canvas */
  --color-surface-container: #f1eee9; /* Soft oatmeal card background */
  --color-surface-low: #f6f3ee;       /* Secondary section alternating fill */
  --color-surface-lowest: #ffffff;    /* Card & modal container surface */
  --color-surface-high: #eae5de;      /* Table headers & strong borders */

  /* Typography Colors */
  --color-on-surface: #1b232c;        /* Deep bistro charcoal (high contrast text) */
  --color-on-surface-variant: #4a5568;/* Slate charcoal (secondary & body text) */
  --color-on-surface-muted: #718096;  /* Meta labels & timestamps */

  /* Brand Accents */
  --color-primary: #881337;           /* Deep Montreal Wine / Bistro Burgundy */
  --color-primary-container: #9f1239; /* Hover state & active highlights */
  --color-secondary: #d97706;         /* Warm Autumn Maple Amber / Gold */
  --color-secondary-container: #fbbf24;/* Warm badge backgrounds */
  --color-accent: #0f766e;            /* Lowcountry / Spruce Slate Teal */

  /* UI & Semantic */
  --color-outline: #718096;
  --color-outline-variant: #cbd5e1;   /* Ghost border line color */
  --color-success: #059669;           /* Confirmed reservations badge */
  --color-warning: #d97706;           /* Active vote status badge */
  --color-error: #b91c1c;             /* Cancelation / alert badge */
}
```

### 2.3 Typography Hierarchy
- **Headlines & Editorial Titles:** `Noto Serif` / `Cormorant Garamond`
  - Hero Display: 64px–84px, font-weight 600/700, tracking tight.
  - Section Headers (H2): 36px–48px, tracking -0.02em.
  - Card Titles (H3/H4): 18px–24px, font-weight 700.
  - Subheaders & French translations: Italic serif (`italic font-serif`).
- **Body & UI Elements:** `Plus Jakarta Sans` / `Inter`
  - Body Text: 14px–16px, line-height 1.6, font-weight 400.
  - Badges, Meta & Microcopy: 10px–12px, font-weight 600, uppercase, tracking 0.08em–0.15em.
- **Accents & Notes:** `Caveat` / Script
  - Polaroid photo captions, family notes, and signature orders.

### 2.4 Shadows & Surfaces
- **Whisper Shadow:** `box-shadow: 0 8px 32px rgba(27, 35, 44, 0.06);`
- **Whisper Shadow LG:** `box-shadow: 0 16px 48px rgba(27, 35, 44, 0.09);`
- **Ghost Border:** `border: 1px solid rgba(203, 213, 225, 0.45);`
- **Border Radius:**
  - Cards & Containers: `rounded-2xl` (16px)
  - Pills & Badges: `rounded-full` (9999px)
  - Micro Badges: `rounded-md` (6px)

---

## 3. Core Component Hierarchy & Layouts

### 3.1 Header / Sticky Identity Bar
- **Live Sync Indicator:** Pulsing green badge showing active state persistence.
- **Voter Switcher Pills:** Horizontal scrollable row of family member names:
  `[Michael] [Haley] [Greg & Cat] [Dani & Travis] [Andrew & Liz] [Michele (Mom)] [Owen & Izzy]`
- **Mode Toggles:** Travis' Fortnite Guide overlay button (`🎮 Travis' Guide`) and Admin Settings button.

### 3.2 Hero & Anchor Stats
- Dramatic full-width hero with atmospheric Montreal autumn photography and dark vignette overlay.
- Large serif title with French bilingual subtitles.
- 4 Key Anchor Cards in glassmorphic overlay:
  1. Basecamp: 3831 St-Laurent (The Plateau)
  2. The Crew: 11 Guests (9 Adults, 2 Kids)
  3. First Touchdown: Thu 4:15 PM (DL4816)
  4. Holiday Constraint: Canadian Thanksgiving (Mon Oct 12)

### 3.3 "L'Arrivée" (Interactive Thursday Arrivals Board)
- Visual 4-step landing timeline for Thursday Oct 8.
- 3-column responsive card grid for each family group displaying:
  - Date & Landing Time badge.
  - Flight number / Transport method.
  - Baggage and Uber coordination notes.
  - "Edit My Arrival" modal trigger.

### 3.4 "Le Plan" (Live Concierge Schedule Matrix)
- 5-day structured itinerary (Thu Oct 8 – Mon Oct 12).
- Desktop: 5-column grid (`Day & Date` | `Morning Coffee` | `Breakfast & Brunch` | `Lunch & Activity` | `Dinner & Night`).
- Mobile: Collapsible adaptive day cards.
- Status Badges:
  - 🟢 **Confirmed & Pinned** (Schwartz's Thu, Departure Mon)
  - 🟡 **Voting Active** (Sat Monarque vs Au Pied de Cochon, Sun Damas vs L'Express)
  - 🔵 **Target Table** (Fri Le Serpent in Old Montreal)
- Admin Edit Mode (PIN `2026`) allowing live changes to themes, booking status, and notes.

### 3.5 "La Carte" (Interactive Master City Map)
- Custom map canvas with CartoDB Voyager tiles.
- Basecamp beacon pulsing at 3831 St-Laurent.
- Color-coded pins for Group Dinners (Wine), Poutine & Casual (Teal), and Attractions (Indigo).
- Filter bar to isolate points of interest.
- Interactive popups with walking/driving times and notes.

### 3.6 "Le Café & La Pâtisserie" (Dedicated Walkable Coffee & Bakery Guide)
- **Coffee Walking Map:** 10-minute walk radius circle (750m) centered on 3831 St-Laurent.
- **Filter Tabs:** `All Walkable Spots` | `☕️ Single-Origin Roasters` | `🥐 Exceptional Baked Goods`
- **Coffee Cards:**
  - High-res imagery of café exterior / latte art.
  - Walking time from basecamp (2–12 min).
  - Specialty tag (e.g. "Single-Origin Multi-Roaster", "Famous Monster Cookies", "Artisanal Simit Bagels").
  - Hours & Yelp rating.
  - **Haley's Coffee Desire Heart Toggle:** Interactive cycle (`🤍🤍` → `❤️` → `❤️❤️`) syncing live.
  - Signature Order callout.

### 3.7 "La Table" (Marquee Group Dinners for 11)
- 6 featured dinner contenders:
  1. *Schwartz's Hebrew Delicatessen* (Thu Arrival · Same Block)
  2. *Le Serpent* (Fri Target · Old Montreal · Closed Sun)
  3. *Monarque* (Sat Contender · Old Montreal · Private Room 22)
  4. *Au Pied de Cochon* (Sat Walkable · 9 min walk)
  5. *Damas* (Sun Splurge · Outremont Syrian)
  6. *L'Express* (Sun / Mon · 8 min walk · Classic Paris Bistro)
- Interactive 👍 / 👎 voting widgets with live voter name badges and counters.

### 3.8 "Alan's Illustrated Guide & Travis' Fortnite Loot Drops"
- 5 category tabs:
  - 🍳 *Breakfast & Bagels* (Eggspectation, Cafeteria, Chez Cora, Place Milton, Fairmount, St-Viateur)
  - 🍟 *Poutine & Casual* (La Banquise 24/7, Frite Alors, Lola Rosa)
  - 🥧 *Desserts & Pastries* (Rockaberry pies, Juliette & Chocolat, Bernie Beigne)
  - 🍻 *Bars & Nightlife* (Bar Bifteck on our block, Brutopia, Benelux, La Distillerie, St. Sulpice, Le Lab)
  - 🍁 *Attractions & Sights* (Mount Royal Observatory, Biodome, Old Port, McGill, Jean-Talon)
- Full upvoting per card.
- **Travis' Victory Royale Mode:** Toggles Fortnite supply drop badges and gamer quote callouts.

### 3.9 "Conseils & Practical Tips"
- 6 structured advice cards:
  - Fee-Free ATMs (Bank of America / Scotiabank)
  - Parking & French Street Cleaning Signs
  - STM Metro & Transit schedules
  - Taxis & Uber Convoys
  - Airbnb Oct 1 Cancellation Lock-in
  - Passports for all 11 travelers

---

## 4. Interaction & Motion Rules
- Smooth scroll navigation across sections (`scroll-smooth`, `scroll-mt-14`).
- Subtle scroll-reveal on intersection (`translate-y-5` to `translate-y-0`, `opacity-0` to `opacity-1` with 0.6s ease).
- Instant optimistic UI on upvotes and coffee hearts with background sync to REST API endpoints (`/api/vote`, `/api/coffee`, `/api/arrival`, `/api/admin/schedule`).
