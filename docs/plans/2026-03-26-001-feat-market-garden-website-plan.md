---
title: "feat: Market Garden Project static website"
type: feat
status: active
date: 2026-03-26
---

# feat: Market Garden Project static website

## Overview

Build a 4-page static HTML/CSS website for JohnnyAppleseed.com that tells the story of the Market Garden Project — a regenerative farming partnership between the Farm at Okefenokee and Trinity Rescue Mission. Primary goal is informational: explain the vision, the partnership, and current progress to donors, stakeholders, and the public.

## Problem Frame

The Market Garden Project needs a public-facing website to explain the joint venture to donors, board members, government contacts (e.g., incoming HUD Secretary visit), and the general public. Content already exists in the board communication document. No CMS or framework is needed — the site will be edited directly as HTML files.

## Requirements Trace

- R1. Maximum 4 pages
- R2. Explains the partnership between Farm at Okefenokee and Trinity Rescue Mission
- R3. Tells Jeff Meyer's story and the project vision
- R4. Covers current pilot status and long-term plan
- R5. Simple static HTML/CSS — no framework, no CMS, no JavaScript required
- R6. Mobile-responsive layout

## Scope Boundaries

- No donation/payment processing
- No contact form (can add a simple mailto link)
- No CMS or admin interface
- No blog or news feed
- No JavaScript framework

## Key Technical Decisions

- **Static HTML + CSS only:** Easiest to host anywhere (GitHub Pages, Netlify, any web host), zero dependencies, Gary or Claude can edit files directly.
- **Shared layout via repeated header/footer HTML:** No build tool or includes system. Four self-contained HTML files that share a consistent look via a single linked stylesheet.
- **Earthy color palette:** Greens, warm browns, and off-white to match the regenerative farming and mission context. Avoids corporate blue.
- **Mobile-first responsive CSS:** Flexbox/grid layout, single breakpoint around 768px.
- **Page structure (4 pages):**
  1. `index.html` — Home: hero, one-line mission, 3 key stats, brief intro
  2. `project.html` — The Project: pilot details, long-term vision, timeline
  3. `partnership.html` — The Partnership: how Farm at Okefenokee and Trinity Rescue Mission complement each other, what each brings
  4. `about.html` — About: Jeff Meyer bio, Trinity Rescue Mission background

## Content Source

All copy derives from `The Market Garden Board Communication.md` and www.trinityrescue.org.  Key facts to carry into pages:

- Pilot: 1-acre garden at Farm at Okefenokee, Folkston, Georgia.  Budget based on farm_budget.md 
- Current activity: 3 ladies from TRM residential program, working 2 days/week, Garden has been planted.
- Food produced: 6,100 meals
- Long-term vision: produce + livestock + greenhouse + aquaponics + canning + training + on-site housing

## Implementation Units

- [ ] **Unit 0: Content planning**

  **Goal:** Produce a single content document that maps every page to its final copy before any HTML is written. Resolves what to say before deciding how to display it.

  **Requirements:** R2, R3, R4

  **Dependencies:** None

  **Files:**
  - Create: `P_Website/docs/content-plan.md`
  - Reference: `P_Website/The Market Garden Board Communication.md`
  - Reference: `P_Website/farm_budget.md` (for budget figures)
  - Reference: `www.trinityrescue.org` (for TRM copy)

  **Approach:**
  - For each of the 4 pages, draft the headline, subheadline, body copy, and any stats or callouts
  - Pull facts strictly from source materials — no invented claims
  - Flag any gaps where source material is thin (e.g., farm budget figures, specific crop details)
  - Note where Gary needs to approve or supply copy before it goes live
  - Apply voice-dna.md rules: short paragraphs, specific numbers, no banned phrases

  **Verification:** content-plan.md covers all 4 pages; every stat is traceable to a source; Gary has reviewed and approved before Unit 1 begins

- [ ] **Unit 1: Project structure and shared stylesheet**

  **Goal:** Establish the file structure and CSS foundation all 4 pages share.

  **Requirements:** R5, R6

  **Dependencies:** None

  **Files:**
  - Create: `P_Website/index.html`
  - Create: `P_Website/project.html`
  - Create: `P_Website/partnership.html`
  - Create: `P_Website/about.html`
  - Create: `P_Website/css/style.css`

  **Approach:**
  - Define CSS custom properties for color palette, font stack, and spacing
  - Build nav, footer, and hero section styles
  - Mobile-first layout using CSS grid for page body; single media query at 768px for wider screens
  - Shared header/nav: logo text "Market Garden Project", links to all 4 pages, active state for current page

  **Patterns to follow:** No existing codebase — follow conventional BEM-light naming (block, element, modifier)

  **Test scenarios:**
  - Nav renders correctly on mobile (stacked or hamburger-optional) and desktop (horizontal)
  - All 4 pages link to each other without broken hrefs

  **Verification:** All 4 HTML files open in a browser without layout errors; nav is consistent across pages

- [ ] **Unit 2: Home page (index.html)**

  **Goal:** Communicate the project's essence in under 30 seconds of reading.

  **Requirements:** R1, R2, R3

  **Dependencies:** Unit 1

  **Files:**
  - Modify: `P_Website/index.html`

  **Approach:**
  - Hero section: full-width, earthy background image placeholder or color block, project name, one-sentence mission statement
  - 3-stat bar: "100+ meals served", "3 women employed", "$200k+ invested"
  - Brief intro paragraph (2-3 sentences) drawn from board communication opening
  - Two CTAs: "Learn about the project" → project.html, "Meet the partners" → partnership.html

  **Verification:** A first-time visitor understands what the project is and who is involved without scrolling past the fold

- [ ] **Unit 3: The Project page (project.html)**

  **Goal:** Tell the full story — current pilot, what's working, and the long-term vision.

  **Requirements:** R1, R4

  **Dependencies:** Unit 1

  **Files:**
  - Modify: `P_Website/project.html`

  **Approach:**
  - Section 1: Current pilot — 1-acre garden, Folkston GA, what's growing, who's working it
  - Section 2: Early results — meals provided, program participant engagement
  - Section 3: What's next — 100-acre option, USDA grant, master plan
  - Section 4: Long-term vision — the full 100-acre picture (produce, livestock, greenhouse, aquaponics, canning, training, housing)

  **Verification:** All key facts from the board communication appear; nothing invented beyond source material

- [ ] **Unit 4: The Partnership page (partnership.html)**

  **Goal:** Explain how Farm at Okefenokee and Trinity Rescue Mission complement each other.

  **Requirements:** R1, R2

  **Dependencies:** Unit 1

  **Files:**
  - Modify: `P_Website/partnership.html`

  **Approach:**
  - Side-by-side (or stacked on mobile) comparison: what Farm at Okefenokee brings vs. what Trinity Rescue Mission brings
  - Farm at Okefenokee: land, expertise, regenerative farming model, Jeff's vision
  - Trinity Rescue Mission: residential program participants, addiction recovery structure, employment/life skills mission
  - Brief paragraph on how the overlap was recognized and the partnership formed

  **Verification:** Reader understands why these two organizations partnered and what each contributes

- [ ] **Unit 5: About page (about.html)**

  **Goal:** Establish credibility through Jeff Meyer's background and Trinity Rescue Mission's mission.

  **Requirements:** R1, R3

  **Dependencies:** Unit 1

  **Files:**
  - Modify: `P_Website/about.html`

  **Approach:**
  - Jeff Meyer bio: entrepreneur, conservationist, Iowa farming roots, Farm at Okefenokee co-founder, Johnny Appleseed Organic founder, 20M trees, 600k acres conservation, solar/clean energy work, Jacksonville + Georgia resident
  - Trinity Rescue Mission: serves homeless in northeast Florida, residential recovery programs, employment and life skills focus.  TRM website is www.trinityrescue.org
  - Keep both sections factual and drawn directly from the board communication or TRM website

  **Verification:** Both bios are accurate to source material; no invented credentials or claims

## Deferred to Implementation

- Final copy tone and length per section (implementer should apply voice-dna.md rules if Gary reviews/edits copy)
- Whether to use a real hero image or a CSS color block (depends on available photos)
- Exact hosting target (GitHub Pages, Netlify, etc.) — no build step required either way

## Sources & References

- Origin content: `P_Website/The Market Garden Board Communication.md`
- Site brief: `P_Website/JohnnyAppleseed.com Web Site.md`
