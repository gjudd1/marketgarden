"""Switch every Give button on partnership.html and phase-one.html between two modes.

  python giving_links.py inpage    FundraiseUp checkout opens on johnnyappleseed.com
  python giving_links.py external  Give buttons link out to trinityrescue.org

inpage mode puts the FundraiseUp installation code (org ABKLWCBV, the same snippet
trinityrescue.org runs) before </body> and points each Give button at ?form=FUNARAUDRDS
on the current page. The widget reads that parameter on load and opens the Phase One
checkout as a modal over the page. For this to work, johnnyappleseed.com has to be an
allowed domain in FundraiseUp (Settings, Installation) on TRM's account. If the domain
is not allowed, the widget does not load and the ?form link does nothing, so check it
on the live page after pushing.

external mode removes the snippet and points each Give button at
https://www.trinityrescue.org/?form=FUNARAUDRDS in a new tab.

Talk to us buttons (mailto to Michael) are not touched. Run it, then commit and push.
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = [os.path.join(HERE, "partnership.html"), os.path.join(HERE, "phase-one.html")]
FORM = "FUNARAUDRDS"

INPAGE_HREF = f'href="?form={FORM}"'
EXTERNAL_HREF = f'href="https://www.trinityrescue.org/?form={FORM}" target="_blank" rel="noopener"'
MAILTO_HREF = 'href="mailto:mmesser@trinityrescue.org?subject=Give%20to%20Phase%20One"'

SNIPPET = """
<!-- Fundraise Up installation, same as trinityrescue.org (org ABKLWCBV). Give buttons open ?form=FUNARAUDRDS on this page. -->
<script>(function(w,d,s,n,a){var o=function(n){return'function'==typeof n?
o.l.push([arguments])&&o:function(){return o.l.push([n,arguments])&&o;}},t
=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;j.src=
'https://cdn.fundraiseup.com/widget/'+a;t.parentNode.insertBefore(j,t);
o.s=Date.now();o.v=3;o.l=[];l='call,catch,on,once,set,then,track'
.split(',');for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=w[n] || o;
})(window,document,'script','FundraiseUp','ABKLWCBV');</script>
</body>"""
SNIPPET_RE = re.compile(r"\n<!-- Fundraise Up installation.*?</script>\n</body>", re.S)


def swap(path, mode):
    s = io.open(path, encoding="utf-8").read()
    n = 0
    for old in (INPAGE_HREF, EXTERNAL_HREF, MAILTO_HREF):
        n += s.count(old)
    if n == 0 and not SNIPPET_RE.search(s):
        print(f"{os.path.basename(path)}: no Give buttons, skipped")
        return
    s = s.replace(EXTERNAL_HREF, INPAGE_HREF).replace(MAILTO_HREF, INPAGE_HREF)
    s = SNIPPET_RE.sub("\n</body>", s)
    if mode == "inpage":
        s = s.replace("\n</body>", SNIPPET, 1)
    else:
        s = s.replace(INPAGE_HREF, EXTERNAL_HREF)
    io.open(path, "w", encoding="utf-8", newline="\n").write(s)
    print(f"{os.path.basename(path)}: {n} Give buttons set to {mode}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode not in ("inpage", "external"):
        sys.exit("usage: python giving_links.py inpage|external")
    targets = PAGES + [p for p in sys.argv[2:]]
    for p in targets:
        if os.path.exists(p):
            swap(p, mode)
