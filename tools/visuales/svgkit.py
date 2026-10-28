# Utilidades para dibujar ilustraciones SVG de las lecciones (convención .as-svg__*, ver js/sanitize.js).
# Paleta (styles.css): ink = negro, warm/sun = amarillo, soft = amarillo claro, fill = acento de la familia, cool = azul.
import math

def svg(title, body, vb="0 0 320 200"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" class="as-svg" role="img"><title>{title}</title>{body}</svg>'

BG = '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__soft"/>'

def arrow_def(lid):
    return (f'<defs><marker id="{lid}-ah" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0L10 5L0 10z" class="as-svg__accent"/></marker></defs>')

def arrow(lid, x1, y1, x2, y2, w=2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="as-svg__ink as-svg__accent" stroke-width="{w}" marker-end="url(#{lid}-ah)"/>'

def text(x, y, s, size=16, anchor="middle", muted=False):
    cls = "as-svg__muted" if muted else "as-svg__label"
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" font-size="{size}">{s}</text>'

def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")

def poly(pts, cls):
    return f'<polygon points="{" ".join(f(x) + "," + f(y) for x, y in pts)}" class="{cls}"/>'

def moon(x, y, r, kind):
    """Luna vista desde el hemisferio sur: la creciente se ilumina a la izquierda (forma de C)."""
    out = f'<circle cx="{x}" cy="{y}" r="{r}" class="as-svg__ink"/>'
    top, bot = f"{x} {y - r}", f"{x} {y + r}"
    if kind == "nueva":
        return out
    if kind == "llena":
        return f'<circle cx="{x}" cy="{y}" r="{r}" class="as-svg__sun"/>' + out
    k = {"creciente": r * 0.55, "menguante": r * 0.55, "cuarto-c": 0, "cuarto-m": 0, "gibosa-c": r * 0.55, "gibosa-m": r * 0.55}[kind]
    left = kind in ("creciente", "cuarto-c", "gibosa-c")
    outer = f"A {r} {r} 0 0 0 {bot}" if left else f"A {r} {r} 0 0 1 {bot}"
    if kind.startswith("cuarto"):
        d = f"M {top} {outer} Z"
    else:
        gib = kind.startswith("gibosa")
        sweep = (0 if left else 1) if gib else (1 if left else 0)
        d = f"M {top} {outer} A {f(k)} {r} 0 0 {sweep} {top} Z"
    return f'<path d="{d}" class="as-svg__sun"/>' + out

def arch(cx, cy, r1, r2, n=9, key_cls="as-svg__fill"):
    """Arco semicircular de n dovelas; la central (clave) con otra clase."""
    out = []
    for i in range(n):
        a0, a1 = math.pi * i / n, math.pi * (i + 1) / n
        pts = [(cx - r2 * math.cos(a0), cy - r2 * math.sin(a0)), (cx - r2 * math.cos(a1), cy - r2 * math.sin(a1)),
               (cx - r1 * math.cos(a1), cy - r1 * math.sin(a1)), (cx - r1 * math.cos(a0), cy - r1 * math.sin(a0))]
        cls = key_cls if i == n // 2 else "as-svg__warm"
        out.append(poly(pts, cls) + poly(pts, "as-svg__ink"))
    return "".join(out)

def sat(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<rect x="-9" y="-9" width="18" height="18" rx="3" class="as-svg__fill"/><rect x="-9" y="-9" width="18" height="18" rx="3" class="as-svg__ink"/>'
            '<rect x="-35" y="-6" width="22" height="12" class="as-svg__warm"/><rect x="-35" y="-6" width="22" height="12" class="as-svg__ink"/>'
            '<rect x="13" y="-6" width="22" height="12" class="as-svg__warm"/><rect x="13" y="-6" width="22" height="12" class="as-svg__ink"/>'
            '<line x1="-13" y1="0" x2="-9" y2="0" class="as-svg__ink"/><line x1="9" y1="0" x2="13" y2="0" class="as-svg__ink"/></g>')

def phone(x, y, s=1.0, pin=True):
    p = (f'<g transform="translate({x},{y}) scale({s})">'
         '<rect x="-18" y="-32" width="36" height="64" rx="7" class="as-svg__ink"/><rect x="-13" y="-24" width="26" height="44" rx="2" class="as-svg__warm"/>')
    if pin:
        p += '<path d="M0 6 C-8 -4 -8 -14 0 -14 C8 -14 8 -4 0 6 Z" class="as-svg__fill"/><circle cx="0" cy="-8" r="2.5" class="as-svg__soft"/>'
    return p + '</g>'

def book(x, y, w=70, h=90, cls="as-svg__warm"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="{cls}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="as-svg__ink"/>'
            f'<line x1="{x + 8}" y1="{y}" x2="{x + 8}" y2="{y + h}" class="as-svg__ink"/>')

def waves(x0, x1, y, amp=6, step=24, cls="as-svg__coolline"):
    d = f"M{x0} {y}"
    x = x0
    while x < x1:
        d += f" q{step / 4} {-amp} {step / 2} 0 t{step / 2} 0"
        x += step
    return f'<path d="{d}" class="{cls}"/>'
