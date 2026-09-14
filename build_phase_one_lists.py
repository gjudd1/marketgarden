"""Regenerate the priced lists on phase-one.html from the current Farm Phase 1 Price List.

  python build_phase_one_lists.py            uses the highest-numbered price list .md
  python build_phase_one_lists.py v9         uses that version

Source: ..\\Project - Farm Sponsorship Package\\Farm Phase 1 Price List (Draft) vN.md
Rewrites three marked blocks in phase-one.html:
  LEVELS  the Sponsorship Levels table (Give up to GIVE_MAX, Talk to us above)
  ITEMS   the Additional Items cards, with photos matched by ITEM_PHOTOS
  BLOCKS  the Phase 1 Total table
and the sentence that carries the additional-items total. The land-shares footnote from the price list is not published (decision 2026-09-12). Everything else on the page is
hand-written prose from the brochure and stays put. Edit the price list, run this, then
commit and push. The numbers on the page never get edited by hand.
"""
import glob, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.join(os.path.dirname(HERE), "Project - Farm Sponsorship Package")
PAGE = os.path.join(HERE, "phase-one.html")
GIVE_MAX = 22_000
GIVE = 'href="?form=FUNARAUDRDS"'
TALK = 'href="mailto:mmesser@trinityrescue.org?subject=Phase%20One%20sponsorship"'

# item name (lowercase substring) -> photo in img/. Items with no match get a plain labeled tile.
ITEM_PHOTOS = [
    ("chick", "img/tier-100-chicks.jpg", "Baby chicks in a wooden crate"),
    ("clothing", "img/tier-500-farm-work.jpg", "Two women in farm aprons holding garden tool buckets"),
    ("laying box", "img/tier-500-laying-hen.jpg", "A roll-out nest box with eggs collected in the front tray"),
    ("nest box", "img/tier-500-laying-hen.jpg", "A roll-out nest box with eggs collected in the front tray"),
    ("meishan", "img/tier-1000-meishan-sow.jpg", "A woman with a Meishan sow in a pasture"),
    ("livestock waterer", "img/sponsor-livestock-waterer.jpg", "Cattle drinking at a metal trough"),
    ("pig field shelter", "img/sponsor-pig-shelter.jpg", "Pigs resting under a field shelter"),
    ("brooder", "img/sponsor-brooder-box.jpg", "Chicks under a heat lamp in a brooder box"),
    ("mobile chicken coop", "img/sponsor-mobile-coop.jpg", "A chicken coop on pasture"),
    ("heirloom seed", "img/sponsor-heirloom-seed.jpg", "Labeled trays of heirloom seedlings"),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def money(s):
    return int(re.sub(r"[^\d]", "", s))


def tables(md):
    """Return {heading: (intro_lines, rows)} for every ## section holding a pipe table."""
    out, head, intro, rows = {}, None, [], []
    for line in md.splitlines():
        if line.startswith("## "):
            if head: out[head] = (intro, rows)
            head, intro, rows = line[3:].strip(), [], []
        elif line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "): continue
            rows.append(cells)
        elif head and line.strip():
            intro.append(line.strip())
    if head: out[head] = (intro, rows)
    return out


def replace_block(page, name, html):
    a, b = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    i, j = page.index(a) + len(a), page.index(b)
    return page[:i] + "\n" + html + "\n" + page[j:]


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else None
    files = glob.glob(os.path.join(PKG, "Farm Phase 1 Price List (Draft) v*.md"))
    ver = lambda f: int(re.search(r"v(\d+)\.md$", f).group(1))
    src = [f for f in files if want is None or f.endswith(f"{want}.md")]
    src = max(src, key=ver)
    md = io.open(src, encoding="utf-8").read()
    t = tables(md)
    print("source:", os.path.basename(src))

    # Sponsorship levels
    intro, rows = t["Sponsorship Levels"]
    body = rows[1:]
    tr = []
    for lvl, what, units in body:
        act = (f'<a class="btn btn-primary btn-sm" {GIVE}>Give</a>' if money(lvl) <= GIVE_MAX
               else f'<a class="btn btn-ghost btn-sm" {TALK}>Talk to us</a>')
        tr.append(f'          <tr><td class="lvl">{esc(lvl)}</td><td>{esc(what)}</td><td class="units">{esc(units)}</td><td class="act">{act}</td></tr>')
    levels_html = "\n".join(tr)

    # Additional items
    ihead = "Additional Items" if "Additional Items" in t else next(h for h in t if "Priority 2" in h)
    intro2, rows2 = t[ihead]
    cards = []
    for item, unit, needed, total, narr in rows2[1:]:
        if item.lower() == "total": continue
        photo = None
        for key, path, alt in ITEM_PHOTOS:
            if key in item.lower():
                photo = (path, alt); break
        ph = (f'<div class="photo"><img src="{photo[0]}" alt="{esc(photo[1])}"></div>' if photo
              else f'<div class="photo none" data-label="{esc(item)}"></div>')
        cards.append(f'''      <article class="item">
        {ph}
        <div class="body">
          <div class="price">{esc(unit)} <small>{esc(needed)} needed</small></div>
          <h4>{esc(item)}</h4>
          <p>{esc(narr)}</p>
          <a class="btn btn-primary btn-sm" {GIVE}>Give</a>
        </div>
      </article>''')
    items_html = "\n".join(cards)
    items_total = next(r[3] for r in rows2 if r[0].lower() == "total")

    # Phase 1 total blocks
    _, rows3 = t["Phase 1 Total"]
    labels = {
        "Priority 1 capital": "Capital: land, buildings, fencing, equipment, wells and site work",
        "Operations, year one": "Operations, year one: wages, managers, feed, fuel, fertilizer and soil",
        "Contingency": "Contingency",
        "Additional items": "Additional items: livestock, tools, coops and small equipment",
        "Priority 2 items": "Additional items: livestock, tools, coops and small equipment",
    }
    br = []
    for block, amt in rows3[1:]:
        if block.startswith("Phase 1"):
            br.append(f'        <tr class="total"><td>Phase One</td><td class="n">{esc(amt)}</td></tr>')
        else:
            br.append(f'        <tr><td>{esc(labels.get(block, block))}</td><td class="n">{esc(amt)}</td></tr>')
    blocks_html = "\n".join(br)

    page = io.open(PAGE, encoding="utf-8").read()
    page = replace_block(page, "LEVELS", levels_html)
    page = replace_block(page, "ITEMS", items_html)
    page = replace_block(page, "BLOCKS", blocks_html)
    page = re.sub(r'(<!-- ITEMS-TOTAL:start -->).*?(<!-- ITEMS-TOTAL:end -->)',
                  lambda m: m.group(1) + f"Together they are the {esc(items_total)} block of Phase One." + m.group(2), page, count=1, flags=re.S)
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(page)
    print(f"levels: {len(body)} rows, items: {len(cards)} cards, blocks: {len(br)} rows, items total {items_total}")


if __name__ == "__main__":
    main()
