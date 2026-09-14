# Project Context — Market Garden Website (JohnnyAppleseed.com)

**Role:** Executive Director, TRM

**Relationship to other projects:**
- Sub-component of `Project - Market Garden` / Regenerative Farm Project — website tells that story
- Content depends on farm letter and budget updates from Market Garden project
- Journal entries (pilot.html) require photos from Barbara; update every 2 weeks

**Problem / Opportunity:**
The Market Garden partnership needs a public-facing site for donors, board members, government contacts, and the general public. Content already exists; the site is live and needs ongoing updates.

**Scope:**
- 5-page static HTML/CSS site: index, pilot, phase-one, about (the two organizations), partnership (the Trembling Earth premiere page, the URL printed on the flyer; post-event handling decided the week of 2026-11-09)
- Hosted via git; deployed via `git push`
- "From the Field" journal on pilot.html — entry every 2 weeks with photos from Barbara
- No CMS, no payment processing, no JavaScript framework
- Tickets go out to Ticketmaster (event 2200651C95EF34CC). Every Give button opens TRM's FundraiseUp checkout in place: the installation code (org ABKLWCBV, same as trinityrescue.org) is on partnership.html and phase-one.html and the buttons point at ?form=FUNARAUDRDS (Phase One designation, from Michael 2026-09-12). johnnyappleseed.com must be an allowed domain in FundraiseUp's installation settings. giving_links.py switches between in-page and linking out to trinityrescue.org. Talk to us buttons are mailto:mmesser@trinityrescue.org
- Meal counter: 30,000 of a 25,000 goal since 2026-09-12 (Darrell); the goal line has not been reset

**Ideas:**
- Phase 2/3 cost structure on the site once those price lists exist
- Customize pitch for family offices vs. general donors

**Barriers / Blockers:**
- Farm letter and updated budget need to be drafted first — website content updates depend on them
- Photos come from Barbara via text; requires proactive reminder to Barb
