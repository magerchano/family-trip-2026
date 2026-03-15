# Family Trip Comparison Page — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a single-page editorial travel comparison site for a family trip vote, deployable on Replit.

**Architecture:** Single `index.html` with embedded `<style>` and `<script>`. Google Fonts for typography. Unsplash for photos. localStorage for scorecard persistence with marked swap point for Replit DB. No frameworks, no build tools.

**Tech Stack:** HTML, CSS, vanilla JS, Google Fonts (Cormorant Garamond, DM Sans)

---

### Task 1: Scaffold HTML and Global Styles

**Files:**
- Create: `index.html`

**Step 1: Create the HTML boilerplate**

Set up `<!DOCTYPE html>`, meta viewport, Google Fonts link for Cormorant Garamond (400, 700) and DM Sans (400, 500, 700). Add empty `<style>` and `<script>` blocks.

**Step 2: Write CSS reset and design tokens**

CSS custom properties for the full palette:
- `--sand`, `--cream`, `--white`, `--charcoal`, `--gray-light`, `--gray-warm` (neutrals)
- `--charleston-accent` deep teal `#1a7a8a`
- `--keys-accent` warm terracotta `#c4654a`
- Typography: `--font-display: 'Cormorant Garamond', serif` and `--font-body: 'DM Sans', sans-serif`
- Spacing scale, max content width `700px`, max section width `1100px`

Global styles: box-sizing reset, body font, base colors, responsive container class, link styles.

**Step 3: Verify in browser**

Open `index.html` in browser. Should see blank page with correct background color and no console errors.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Scaffold HTML boilerplate with design tokens and global styles"
```

---

### Task 2: Hero Section

**Files:**
- Modify: `index.html`

**Step 1: Write hero HTML**

Full-viewport `<section class="hero">` with:
- Cinematic background image (Unsplash aerial coastline/ocean: `https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1600&q=80`)
- `<h1>` with "Summer 2026" in Cormorant Garamond
- `<p>` subline: "Two trips. One family. You decide."
- Two `<a>` pill buttons: "Charleston + Kiawah" linking to `#charleston`, "Keys + Everglades" linking to `#keys`

**Step 2: Write hero CSS**

- `min-height: 100vh`, background-image with `cover`, dark overlay via `::before` pseudo-element
- Centered flex layout for content
- Headline: white, large clamp-based font-size, Cormorant Garamond weight 700
- Subline: white with slight transparency, DM Sans
- Pill buttons: transparent with white border, white text, border-radius 50px, hover fills white with dark text
- Subtle fade-up animation on load via `@keyframes` and `animation-delay` staggering

**Step 3: Verify in browser**

Full-screen hero with photo, readable text, two clickable pill buttons. Looks good on both desktop and mobile (test by resizing).

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add hero section with background photo and navigation pills"
```

---

### Task 3: Charleston + Kiawah — Photo Opener and Pitch

**Files:**
- Modify: `index.html`

**Step 1: Write trip opener HTML**

`<section id="charleston">` with:
- Full-width image container with Unsplash Charleston photo (historic district or waterfront)
- Overlaid trip name "Charleston + Kiawah Island" in display serif
- Tagline beneath: "Michelin stars, dolphin charters, and resort life done right."
- Pitch paragraph block (narrow centered column): the 2-3 sentence summary from the content about best blend of resort stay, family logistics, Michelin credibility

**Step 2: Write CSS for trip opener pattern**

- Full-width image with dark gradient overlay for text readability
- Overlaid text: white, large serif, absolute positioned over image
- `.trip-pitch` class: max-width 700px, centered, larger body text (1.15rem), generous line-height (1.8), padding top/bottom

**Step 3: Verify in browser**

Scroll past hero, see full-width Charleston photo with title overlay, then a clean centered pitch paragraph.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add Charleston trip opener with photo and pitch"
```

---

### Task 4: Charleston — Stay Plan Cards

**Files:**
- Modify: `index.html`

**Step 1: Write stay cards HTML**

Two-column grid inside the Charleston section:
- Card 1: "Nights 1–3" label, "The Charleston Place" heading, description about polished city base, two-bedroom suites
- Card 2: "Nights 4–7" label, "Kiawah Island Resort Villa" heading, description about 3+ bedroom villa, resort access, pools, beach

**Step 2: Write stay card CSS**

- Two-column grid with gap, single column on mobile
- Cards: subtle border (1px solid light gray), no heavy shadow, generous padding
- Night label: small uppercase tracking, teal accent color
- Heading: Cormorant Garamond, medium size
- Description: DM Sans, smaller, muted color

**Step 3: Verify in browser**

Two clean cards side by side on desktop, stacked on mobile.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add Charleston stay plan cards"
```

---

### Task 5: Charleston — Day-by-Day Timeline

**Files:**
- Modify: `index.html`

**Step 1: Write timeline HTML**

Section heading "Day by Day" centered. Then 8 day entries, each containing:
- Day number in accent color (teal)
- Short title (e.g., "Arrive & Settle Into Charleston")
- Expandable detail block (hidden by default) with the full day description from the pasted content
- A subtle toggle indicator (+ / −)

All 8 days from the Charleston itinerary with full content.

**Step 2: Write timeline CSS**

- Vertical left border or rule connecting days
- Day number: Cormorant Garamond, teal, positioned left
- Title: DM Sans weight 600, inline with day number
- Thin ruled line (1px solid light gray) between entries
- Detail block: `max-height: 0; overflow: hidden; transition: max-height 0.4s ease`
- `.open` state: `max-height: 300px`
- Toggle indicator: small, muted, rotates on open

**Step 3: Write toggle JS**

```js
function toggleDay(header) {
  const card = header.closest('.day-entry');
  card.classList.toggle('open');
}
```

Attach via `onclick` on each day header.

**Step 4: Verify in browser**

8 collapsed day rows. Click each to expand/collapse. Content matches the itinerary.

**Step 5: Commit**

```bash
git add index.html
git commit -m "Add Charleston day-by-day expandable timeline"
```

---

### Task 6: Charleston — Dining Section

**Files:**
- Modify: `index.html`

**Step 1: Write dining HTML**

Section heading "The Food" centered, with subline "Charleston's Michelin lineup is no joke."

Two-column layout:
- Left column "Special Dinners": Wild Common (★ 1 Star), Vern's (★ 1 Star), Malagón (★ 1 Star), Sorelle (Michelin Listed) — each with name, pill tag, one-line description
- Right column "Family-Friendly": Leon's Oyster Shop, Lewis Barbecue, Rodney Scott's BBQ, FIG — each with name, tag, description

**Step 2: Write dining CSS**

- Two-column grid, single column on mobile
- Column header: Cormorant Garamond, small, with dashed border-bottom in accent color
- Restaurant name: DM Sans weight 700
- Tags: small pill badges — gold/amber for star, coral for Bib, green for family-friendly
- Description: small muted text beneath name
- Thin ruled lines between items

**Step 3: Verify in browser**

Clean menu-style dining guide. Tags are readable and tasteful.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add Charleston dining section with Michelin tags"
```

---

### Task 7: Keys + Everglades — Full Trip Section

**Files:**
- Modify: `index.html`

**Step 1: Build the entire Keys section**

Replicate the exact same structure as Tasks 3-6 but for the Keys + Everglades trip:
- Photo opener with Keys/tropical photo, title overlay, tagline: "Reef snorkeling, airboats, and alligators that don't care about your plans."
- Pitch paragraph about the adventure-forward trip, coral reef, Everglades
- Stay cards: Four Seasons at The Surf Club (Nights 1–2), Cheeca Lodge & Spa (Nights 3–7)
- Day-by-day timeline: all 8 days with full content, using coral/terracotta accent color
- Dining section: The Surf Club Restaurant (1 Star), Cote Miami (1 Star), Michael's Genuine (Bib Gourmand, Family Friendly), Keys casual dining

Use the coral/terracotta accent color (`--keys-accent`) throughout instead of teal.

**Step 2: Verify in browser**

Both trip sections have identical structure, equal visual weight. Accent colors differentiate them. All day entries expand/collapse.

**Step 3: Commit**

```bash
git add index.html
git commit -m "Add Keys + Everglades trip section mirroring Charleston structure"
```

---

### Task 8: The Honest Comparison Section

**Files:**
- Modify: `index.html`

**Step 1: Write comparison HTML**

New section with subtle warm gray background (`--gray-warm`).
- Heading: "The Honest Comparison"
- Two-column grid:
  - Left column: "Charleston + Kiawah" header in teal. Pros with `+` prefix, cons with `−` prefix. All bullet points from the pasted content.
  - Right column: "Keys + Everglades" header in coral. Same format.
- Below columns: centered "Bottom Line" paragraph summarizing the trade-off.

**Step 2: Write comparison CSS**

- Background color shift to `--gray-warm`
- Two-column grid, stacked on mobile
- Column headers in respective accent colors
- `+` and `−` prefixes in accent color, bold
- Items separated by thin ruled lines
- Bottom line paragraph: narrow centered column, slightly larger text

**Step 3: Verify in browser**

Clean comparison. Both columns feel equal. Readable on mobile when stacked.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add honest comparison section with pros, cons, and bottom line"
```

---

### Task 9: The Scorecard — HTML and Scoring UI

**Files:**
- Modify: `index.html`

**Step 1: Write scorecard HTML**

Continues on warm gray background. Wrapped in `<!-- SCORECARD START -->` / `<!-- SCORECARD END -->` comments for easy removal.

- Heading: "Rate Each Trip" in display serif
- Voter dropdown: select with options for Jan, Haley, Michael, Trey, Katy
- Scoring grid: a table/grid with 6 category rows. Each row has:
  - Category name on the left
  - 5 clickable circles for Charleston score (teal)
  - 5 clickable circles for Keys score (coral)
- Submit button: clean outlined style

**Step 2: Write scorecard CSS**

- Score circles: small (20px), border in accent color, empty by default, filled on click
- Active/selected circles: filled with accent color
- Grid layout: category label left, Charleston circles center-left, Keys circles center-right
- Responsive: on mobile, each category stacks as category name, then Charleston row, then Keys row
- Submit button: outlined, accent color border, fills on hover

**Step 3: Verify in browser**

Can see all 6 categories with clickable circle ratings for both trips. Circles fill when clicked.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add scorecard UI with 6 categories and rating circles"
```

---

### Task 10: The Scorecard — JS Logic and Results Display

**Files:**
- Modify: `index.html`

**Step 1: Write scoring JS**

```js
// Data structure in localStorage:
// { "jan": { "charleston": { "food": 4, "activities": 3, ... }, "keys": { ... } }, ... }
```

Functions:
- `selectScore(voter, trip, category, score)` — updates in-memory state and highlights circles
- `submitScores()` — validates all categories are scored, saves to localStorage
- `getScores()` / `saveScores()` — localStorage read/write with `familyTrip2026Scores` key
- `updateResults()` — calculates per-voter totals and cross-voter averages, updates display

Circle click handlers: clicking circle N fills circles 1 through N (like a star rating).

**Step 2: Write results display HTML**

Below the scoring grid:
- Results table: categories down the left, average Charleston score and average Keys score columns
- Total row at bottom with sum
- Individual voter breakdown: small text showing each person's totals
- "No scores yet" placeholder when empty

**Step 3: Write results CSS**

- Clean table styling: thin borders, accent color headers
- Total row: slightly bolder
- Voter breakdown: smaller text, muted

**Step 4: Verify in browser**

Select a name, click scores for all 6 categories for both trips, submit. Results update. Refresh page — scores persist. Select a different name, score again — averages update.

**Step 5: Commit**

```bash
git add index.html
git commit -m "Add scorecard JS logic with localStorage persistence and results display"
```

---

### Task 11: Scroll Reveal Animations

**Files:**
- Modify: `index.html`

**Step 1: Add reveal CSS class**

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**Step 2: Add `.reveal` class to major content blocks**

Trip headers, stay cards, timeline sections, dining sections, comparison columns, scorecard.

**Step 3: Write IntersectionObserver JS**

```js
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
reveals.forEach(el => observer.observe(el));
```

**Step 4: Verify in browser**

Scroll through the page. Sections fade in as they enter the viewport.

**Step 5: Commit**

```bash
git add index.html
git commit -m "Add scroll reveal animations via IntersectionObserver"
```

---

### Task 12: Footer and Final Polish

**Files:**
- Modify: `index.html`

**Step 1: Add footer**

```html
<footer class="site-footer">Made with love and strong opinions about dolphins.</footer>
```

Styled: centered, small text, light gray, generous top padding.

**Step 2: Responsive audit**

Check all sections at 375px (phone), 768px (tablet), 1200px+ (desktop). Fix any layout breaks:
- Photo openers scale properly
- Grids collapse to single column on mobile
- Scorecard circles remain tappable on mobile (min 44px touch target)
- Text is readable at all sizes

**Step 3: Final browser check**

Full scroll-through on desktop and mobile. All interactions work: day toggles, score circles, submit, results display.

**Step 4: Commit**

```bash
git add index.html
git commit -m "Add footer and complete responsive polish"
```

---

### Task 13: Push to GitHub

**Step 1: Create GitHub repo and push**

```bash
gh repo create family-trip-2026 --private --source=. --push
```

**Step 2: Verify on GitHub**

Confirm repo exists with all commits.

**Step 3: User imports into Replit**

User creates a Repl from GitHub repo URL. Site is live.
