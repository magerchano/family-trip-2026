# Kanban Meal Planner Design

**Goal:** Replace the static itinerary with an interactive drag-and-drop kanban board where family members can assign restaurants, activities, and coffee shops to specific days and meal slots.

**Architecture:** Same single index.html. HTML5 native drag-and-drop with touch support. localStorage persistence.

## Layout
- Left sidebar: draggable card pool (restaurants by meal type, activities, coffee shops) with search
- Main board: 6 columns (Mon-Sat June 8-13), each with 5 drop zones (Breakfast, Coffee, Lunch, Dinner, Other)
- Mobile: sidebar becomes top drawer, board scrolls horizontally

## Cards
- Restaurant: name, primary badge, meal type, kid-friendly dot
- Activity: teal left border, name, duration. Items: Kiawah Dolphin Charter, Family Kayaking, Oyster Farm Tour, Bulls Island Ferry, Historic District Walk, King Street Shopping, Beach/Pool Day, Sunset Cruise
- Coffee: gold left border, name, walking distance

## Interaction
- Drag from sidebar to slot, or between slots
- "Proposed by [name]" tag on placed cards
- One item per slot, old item returns to sidebar if replaced
- Cards stay in sidebar (greyed) when placed
- Remove via x button or drag back
- Voter dropdown controls "proposed by" tag

## Persistence
- Key: charlestonTrip2026Planner
- Structure: { "mon-breakfast": { item, type, proposedBy }, ... }
