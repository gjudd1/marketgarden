# Visual Plan: Regenerative Farm Initiative Website

**Last updated:** 2026-04-18  
**Version:** Draft 1.0  
**Scope:** 3-page static site — index.html, pilot.html, partnership.html

---

## 1. Current Site State

The site uses a single CSS file (`css/style.css`) with a handcrafted design system built on CSS custom properties. The palette is warm earth tones: deep forest green, cream, and brown accent. Georgia serif headings, system-ui body text.

**What works:**
- Responsive layout (mobile-first, single breakpoint at 768px)
- Sticky header with navigation
- Hero section with CTA buttons
- Section alternation (white / cream / dark green)
- Cards, tables, stat bar (CSS only — stat bar not yet wired to any page)
- Footer with partner links

**Known issues to fix:**
- "Three Commitments" section (index.html lines 59–78) uses two mismatched 2-column grids — the third card sits in a row with an empty `<div>`, which looks broken on desktop
- `p` tags have `margin-left: auto; margin-right: auto` globally — this centers paragraph text incorrectly in left-aligned card and list contexts
- Stat bar component exists in CSS but is not used on any page (partnership.html is the natural home for Trinity stats)
- No hero image support — hero is pure color block; ready to accept a photo background once images are available
- No mobile hamburger menu — nav wraps awkwardly on small screens
- Interior page headers (`.page-header`) are cream on white — low visual contrast, underwhelming entry point
- Budget section on pilot.html is a bare paragraph — a simple breakdown table would be stronger
- No active-state logic on home page nav link when returning from interior pages (minor)

---

## 2. Visual Themes

Four distinct visual directions to choose from. Only one will be built at a time. Once a direction is selected, a new CSS file (`css/theme-[name].css`) is created and linked in place of `style.css`. The content (HTML) stays the same across all themes.

---

### Theme A — "Earthy Heritage" *(current direction)*

**Character:** Family farm. Roots. Warmth. Heirloom seeds and handwritten recipes.  
**Best for:** Donors who respond to tradition, craft, and place.

| Element | Value |
|---|---|
| Background | Warm cream `#f5f0e8` |
| Primary | Forest green `#2d5a3d` |
| Accent | Warm brown / tan `#c8a882` |
| Headings | Georgia serif |
| Body | System-ui sans |
| Radius | 4px (subtle) |
| Imagery style | Natural light, close-up farm textures, portrait of workers |

**Refinements needed from current version:**
- Fix the three-card layout issue (use CSS Grid 3-col or stack properly)
- Add a thin decorative rule or leaf icon as a section divider
- Increase hero h1 size on desktop to 3.2rem for more presence
- Add a subtle grain texture overlay to the hero background color

---

### Theme B — "Clean Mission"

**Character:** Nonprofit credibility. Professional. Trustworthy. Report-ready.  
**Best for:** Grant writers, institutional donors, board presentations.

| Element | Value |
|---|---|
| Background | White `#ffffff` |
| Primary | Deep slate `#1e3a5f` |
| Accent | Warm orange `#d4622a` |
| Headings | Inter or system-ui, bold, sans-serif |
| Body | System-ui sans |
| Radius | 6px |
| Imagery style | Clean portraits, documentary-style, minimal |

**Key visual differences:**
- Header is white with a bottom border — not a dark band
- Stats on partnership page displayed in bold, large-number format (stat-bar component)
- Buttons are solid filled with no outline variant
- Cards have a left border accent instead of full border
- Section alternation uses a light blue-gray `#f0f4f8` instead of cream

---

### Theme C — "Pastoral / Photo-Forward"

**Character:** Immersive. Story-driven. Emotional. Land and people.  
**Best for:** When photos from the Google Drive album are added. Impact-first storytelling.

| Element | Value |
|---|---|
| Background | Off-white `#faf9f7` |
| Primary | Sage green `#6b8f71` |
| Accent | Dusty gold `#b8962e` |
| Headings | Georgia serif, lighter weight |
| Body | System-ui sans, slightly larger (17px base) |
| Radius | 0 (no rounded corners — raw, honest) |
| Imagery style | Full-bleed hero photo, inline photos between sections |

**Key visual differences:**
- Hero requires a real photo background — text overlaid with a dark gradient
- Sections have full-width divider photos (placeholder until images arrive)
- Typography is larger and more generous — designed to be read slowly
- Cards are removed in favor of generous whitespace and pull-quotes

**Note:** This theme is best activated *after* photos are sourced from the Google Drive album or okefarm.com/trinityrescue.org.

---

### Theme D — "Bold & Simple"

**Character:** Impact. Urgency. Fundraising campaign energy.  
**Best for:** A campaign landing page, major gift ask, or public launch moment.

| Element | Value |
|---|---|
| Background | White `#ffffff` |
| Primary | Almost black `#111111` |
| Accent | Hunter green `#2d5a3d` (same green, used sparingly) |
| Headings | System-ui, heavy weight (800), uppercase |
| Body | System-ui sans |
| Radius | 2px |
| Imagery style | High contrast, bold crop |

**Key visual differences:**
- Header is white/transparent — minimal
- Hero headline is very large (4–5rem on desktop), left-aligned, not centered
- One dominant CTA per page — no secondary buttons
- Stat numbers are huge (4rem+) and the primary content on the partnership page
- No cards — information delivered in plain text with strong typographic hierarchy

---

## 3. Workflow

### Per-session process

1. Review `docs/content-plan.md` for any new content or links before starting work
2. Make changes to HTML and CSS
3. Test in browser — check mobile (narrow window) and desktop
4. Update `docs/content-plan.md` to note what changed, what was added, what is still needed
5. Commit to GitHub with a descriptive message (`git commit -m "..."`)
6. Push to `https://github.com/gjudd1/marketgarden.git`

### Branch / versioning convention

| Use case | Branch name |
|---|---|
| Active development | `main` or `master` |
| Testing a new theme | `theme-[name]` |
| Major content revision | `v2`, `v3`, etc. |
| Hotfix | `fix-[description]` |

Each visual theme lives in its own CSS file so themes can be compared by switching a single `<link>` tag in the HTML.

---

## 4. Photo Integration Plan

**Status: Images selected and copied to `img/` folder — 2026-04-18**

### Image inventory and placement

| File | Subject | Intended placement |
|---|---|---|
| `hero-tomatoes.jpg` | Heirloom tomatoes arranged on wood — spectacular color | Home hero background OR pilot page header |
| `harvest-crates.jpg` | Crates of chard, carrots, radishes, greens — real farm harvest | Home "What the Farm Will Be" OR pilot "Progress to Date" |
| `harvest-table.jpg` | Full harvest spread on table — eggplant, peppers, squash, tomatoes | Home produce section |
| `harvest-cabbage.jpg` | Cabbages, kale, carrots, radishes on weathered wood | Partnership page OR home section |
| `farm-worker.jpg` | Woman sitting with large black pigs — authentic, human | Home "Jobs for Women" commitment card |
| ~~`horse-riding.jpg`~~ | ~~Woman on horseback~~ | ~~Removed — not approved for use~~ |
| `cattle-field.jpg` | Cattle grazing in lush green field — wide landscape | Partnership "Farm at Okefenokee" section |
| `bee-blossom.jpg` | Honeybee on cherry blossom — delicate, ecosystem | Home accent / section break |
| `monarch-caterpillar.jpg` | Monarch caterpillar on milkweed — regeneration symbol | Section accent |
| `monarch-butterfly.jpg` | Monarch butterfly on purple salvia | Section accent |
| `onions-harvest.jpg` | 100+ onions laid out to dry on rack — abundance | Pilot "Progress to Date" section |
| `squash-harvest.jpg` | Yellow squash, zucchini, striped eggplant in crate | Pilot or home produce section |
| `peppers.jpg` | Colorful red/orange/yellow peppers on plant | Accent / card background |
| `baby-piglet.jpg` | Baby piglet portrait — warm, charming | Card or sidebar accent |
| `spaghetti-squash.jpg` | Spaghetti squash in cold storage crate | Pilot budget/operations section |

### Notes
- All images are phone-quality JPGs, 250KB–4.4MB. **Optimize before deploying** (resize to max 1400px wide, JPEG quality 80) to keep page load fast.
- `farm-worker.jpg` and `horse-riding.jpg` are the only images with people from the program — use prominently.
- `hero-tomatoes.jpg` and `harvest-cabbage.jpg` are portrait-oriented — crop or use as right-side panels rather than full-width backgrounds.
- `cattle-field.jpg`, `harvest-crates.jpg`, and `harvest-table.jpg` are landscape — best for hero/banner use.
- Source folder: `C:\Users\gjudd\OneDrive - Trinity Ministries\GaryFiles\Working\Executive Director\Project - Market Garden\Farm Images\APG` (102 images total — 15 selected)

---

## 5. Decisions Needed

| Decision | Options | Status |
|---|---|---|
| Which visual theme to develop first | A (refine current), B, C, D | **Open** |
| Photo sourcing | Google Drive, partner sites, new photos | Pending |
| Site hosting | GitHub Pages, Netlify, other | Pending |
| Site name / domain | TBD | Pending |
| Add a donation/contact CTA | Yes / No | Open |
| Mobile menu | Hamburger toggle (needs JS) / keep wrap | Open |
