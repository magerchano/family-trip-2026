# Family Trip Comparison Page — Design

## Purpose

A single-page website hosted on Replit where family members can compare two summer 2026 trip options and optionally score them. The page presents detailed itineraries for Charleston + Kiawah Island and Florida Keys + Everglades in a fair, visually equal format.

## Audience

Seven family members: Jan, Haley, Michael, Trey, Katy, Jax (~8), Rey (~10). Five adults vote/score. The page will be shared via link — most viewers will be on mobile.

## Aesthetic Direction

Magazine spread / editorial travel feature. Clean, sophisticated, lots of white space. No emoji in content — the playfulness comes from the copy tone, not decoration.

### Typography
- Display/headlines: Cormorant Garamond (serif)
- Body: DM Sans (sans-serif)

### Color Palette
- Neutral base: warm whites, soft grays, charcoal text
- Charleston accent: deep teal
- Keys accent: warm terracotta/coral
- Accents used sparingly in borders, tags, and highlights

## Page Structure

### 1. Hero
- Full-viewport cinematic background photo (aerial coastline)
- Large serif headline: "Summer 2026"
- Subline: "Two trips. One family. You decide."
- Two pill-shaped nav buttons smooth-scrolling to each trip section
- Subtle fade-up entrance animation

### 2. Trip Sections (identical structure, Charleston first)

Each trip section contains:

**Photo opener** — Full-width hero-scale image with trip name overlaid in large serif type and an editorial tagline.

**The Pitch** — 2-3 sentence summary in larger body text, centered in a narrow column (~700px max).

**Where You'll Stay** — Two side-by-side cards with hotel/resort name, number of nights, and brief description. Clean borders, no heavy shadows.

**Day by Day** — Vertical timeline with day number in accent color, short title, and expandable detail block. Collapsed by default. Thin ruled lines between days.

**The Food** — Two-column menu-style layout. Left: special dinners with Michelin star/Bib pill tags. Right: family-friendly picks. Serif names, small sans-serif descriptions.

### 3. The Honest Comparison
- Subtle background shift (warm gray) to separate from trip sections
- Two columns on desktop, stacked on mobile
- Trip name headers in respective accent colors
- Pros marked with + prefix, cons with − prefix, in accent color
- Clean ruled lines between items
- Centered "Bottom Line" editorial summary paragraph below

### 4. The Scorecard
- Same warm gray background
- Centered heading in display serif
- Dropdown to select voter name (Jan, Haley, Michael, Trey, Katy)
- 6 scoring categories, each rated 1–5 for both trips:
  - Food & Dining
  - Activities & Adventure
  - Kid-Friendliness
  - Lodging & Comfort
  - Weather Confidence
  - Overall Excitement
- Input: row of 5 circles, click to fill (accent color)
- Results display:
  - Table with categories down left, Charleston and Keys scores side by side
  - Total row (max 30 per trip per voter)
  - Averaged scores across all voters when multiple have scored
  - Individual voter breakdown below
- Wrapped in HTML comment for easy show/hide
- Uses localStorage with marked swap point for Replit DB

### 5. Footer
- Single centered line, small light gray text
- "Made with love and strong opinions about dolphins."

## Technical Approach
- Single index.html with embedded CSS and JS
- Google Fonts for typography
- Real photos from Unsplash
- localStorage for score persistence (with clear code comments for Replit DB swap)
- Responsive: mobile-first, columns stack on narrow screens
- No build tools, no dependencies, no framework
