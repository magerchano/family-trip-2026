# Charleston Trip Page Redesign

**Goal:** Rebuild the trip comparison page into a single-trip planning doc for Charleston, June 2026. Family trip Mon June 8 – Sat June 13 at Mill House (Hilton points). Couples weekend Sat June 13 – Sun/Mon June 15 at luxury hotel TBD. Includes restaurant dashboard with voting, coffee shop guide, and day-by-day itinerary.

**Architecture:** Single `index.html` with embedded CSS/JS. Same editorial magazine aesthetic (Cormorant Garamond + DM Sans). localStorage for votes/ratings. Hosted on Replit via GitHub.

## Page Sections

- [x] 1. Hero — "Charleston, June 2026"
- [x] 2. Plan at a Glance — visual timeline
- [x] 3. Where We're Staying — Mill House + couples hotel cards
- [x] 4. Day-by-Day Itinerary — family week + couples weekend
- [x] 5. Restaurant Guide — curated cards with voting + master table
- [x] 6. Coffee Guide — cards with Haley's desire toggle
- [x] 7. Footer

## Section Details

### 1. Hero
Clean editorial hero. "Charleston, June 2026" in Cormorant Garamond. Subline like "The plan. The food. The coffee." Background photo of Charleston. No comparison toggle.

### 2. Plan at a Glance
Simple visual timeline showing:
- Sat–Sun June 6–7 OR Sat–Mon June 13–15: Couples weekend (TBD placement)
- Mon–Sat June 8–13: Family trip at Mill House

Show both pre/post options for the couples weekend. Clean horizontal timeline or stacked cards.

### 3. Where We're Staying

**Mill House Hotel (Family):**
- Mon June 8 – Sat June 13
- Hilton points redemption
- Downtown Charleston, Queen Street area

**Couples Weekend Hotel (TBD):**
- Options to present: Zero George (baseline), Wentworth Mansion (upgrade pick), The Spectator (service pick), 86 Cannon (hidden gem)
- Show as cards the user can compare

### 4. Day-by-Day Itinerary

**Family Week (Mon–Sat):**
Activities pool includes:
- Charleston Oyster Farm tour (charlestonoysterfarm.com)
- Kiawah Island day trip — dolphin charter, family kayaking, beach
- Bulls Island wildlife ferry
- Historic district exploring (Rainbow Row, Battery, waterfront)
- Pool/beach days
- Sunset cruise or shelling

**Couples Weekend:**
- Lighter section — fine dining, exploring, relaxation
- Michelin star dinners (Wild Common, Vern's)
- Restaurant at Zero George (if staying there)

### 5. Restaurant Guide

**Curated Cards ("Our Picks") — 10 restaurants with voting:**

Special Dinners (adults):
1. Wild Common — Michelin 1 Star, tasting menu $95pp
2. Chubby Fish — NYT Top 50, James Beard semifinalist, TikTok viral (caviar sliders), no reservations
3. Vern's — Michelin 1 Star, intimate candlelit

Family Dinners:
4. Leon's Oyster Shop — Michelin Bib Gourmand, TikTok, Haley's list
5. Rodney Scott's BBQ — Michelin Bib Gourmand, James Beard winner, TikTok
6. Poogan's Porch — TikTok, Haley's list, classic Southern

Casual/Lunch:
7. Xiao Bao Biscuit — Michelin listed, Haley's list
8. Hometeam BBQ — Haley's list, kid-friendly

Breakfast/Brunch:
9. Callie's Hot Little Biscuit — TikTok, Haley's list

Dessert:
10. Sugar Bakeshop — TikTok viral (121K posts), 20-year institution

Each card: photo, name, one-line pitch, buzz badges (Michelin Star, Bib Gourmand, Michelin Listed, James Beard, NYT Top 50, TikTok Viral, Haley's List), meal type, kid-friendly indicator, vote button.

Voting: 5 voters (Jan, Haley, Michael, Trey, Katy). Heart toggle per restaurant. Shows count + who voted.

**Master Table — all restaurants:**

Columns: Restaurant, Best For (meal), Vibe, Kid-Friendly, Reservations, Booking (platform + window), Buzz (badges)

Filter bar: meal type, kid-friendly toggle, search box.

Full restaurant list (from all sources — Michelin, TikTok, NYT, James Beard, Haley's list):

Michelin Stars: Wild Common, Vern's, Malagón Mercado y Taperia
Bib Gourmand: Rodney Scott's, Lewis Barbecue, Leon's Oyster Shop
Michelin Listed: Chubby Fish, FIG, Husk, Sorelle, Lowland, Xiao Bao Biscuit, The Establishment, The Obstinate Daughter, The Restaurant at Zero George
James Beard 2026: Chubby Fish, Merci, Renzo, Palmira, Bintu Atelier
NYT: Chubby Fish (Top 50), Palmira (Best Dishes)
TikTok/Haley's List: Fleet Landing, Juanitas, Hometeam BBQ, Le Farfalle, Rancho Lewis, The Matador, Goat Sheep Cow, Church and Union, The Peacock, Darling Oyster Bar, Babas, Callie's Hot Little Biscuit, Millers All Day, Poogan's Porch
Dessert: Sugar Bakeshop, Peace Pie, Jeni's, Carmella's
Additional buzz: Sullivan's Fish Camp, Tutti Pizza, Cane Pazzo, Kultura, SHIKI, Volpe's, Hannibal's Kitchen, Jack of Cups, The Daily, Grit Bakery

### 6. Coffee Guide

8 coffee shops as cards. Each card:
- Photo
- Name
- Vibe one-liner
- Hours
- Walking distance from Mill House
- Yelp/Google rating
- TikTok buzz indicator
- Signature order
- Haley's desire toggle: empty (no interest), single heart (want to go), double heart (must go)

Coffee shops:
1. Harken Cafe — 1 min walk, 4.6/5, biscuit sandwiches + pastries
2. The Rise Coffee Bar — 5 min, 4.5/5, most Instagrammable, garden patio
3. Second State Coffee — 5 min, 4.6/5, homegrown specialty roaster
4. Babas on Wentworth — 4 min, 4.5/5, European cafe, peanut mocha
5. Bad Bunnies Coffee — 8 min, 5.0/5, artist-built hidden gem
6. Kudu Coffee — 10 min, 4.6/5, secret garden courtyard
7. Bitty & Beau's — 3 min, 4.8/5, nationally recognized, feel-good
8. The Daily — 12 min, 4.5/5, TikTok king (169K posts)

### 7. Footer
"Made with love and strong opinions about dolphins."
