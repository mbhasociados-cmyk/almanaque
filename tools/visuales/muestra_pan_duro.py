# Muestra de ilustraciones (26-10-2026): pan-duro r2 + diagramas SVG por tarjeta -> borrador r3 (no se publica).
import json, os, sys
ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
from almanaque_lib import validate

def svg(title, body, vb="0 0 320 200"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" class="as-svg" role="img"><title>{title}</title>{body}</svg>'
BG = '<rect x="0" y="0" width="320" height="200" rx="18" class="as-svg__soft"/>'
def pan(x, y, s=1.0):
    # marraqueta: dos "cachitos" unidos, con corte al medio
    return (f'<g transform="translate({x},{y}) scale({s})">'
            '<path d="M0 30 C0 5 40 0 60 12 C80 0 120 5 120 30 C120 55 80 60 60 48 C40 60 0 55 0 30 Z" class="as-svg__warm"/>'
            '<path d="M0 30 C0 5 40 0 60 12 C80 0 120 5 120 30 C120 55 80 60 60 48 C40 60 0 55 0 30 Z" class="as-svg__ink"/>'
            '<path d="M60 14 L60 46" class="as-svg__ink"/><path d="M22 22 q8 -6 16 0" class="as-svg__ink"/><path d="M82 22 q8 -6 16 0" class="as-svg__ink"/></g>')
ARROW = '<defs><marker id="pan-duro-ah" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" class="as-svg__accent"/></marker></defs>'

V = {}
V["c1"] = svg("Una marraqueta de la mañana y la misma marraqueta en la tarde",
    BG + pan(30, 70) + pan(170, 70) +
    '<circle cx="90" cy="40" r="16" class="as-svg__sun"/><text x="90" y="160" text-anchor="middle" class="as-svg__label" font-size="17">mañana</text>'
    '<circle cx="230" cy="40" r="16" class="as-svg__fill"/><text x="230" y="160" text-anchor="middle" class="as-svg__label" font-size="17">tarde</text>'
    '<text x="160" y="190" text-anchor="middle" class="as-svg__muted" font-size="16">¿qué cambió?</text>')
# almidón: desordenado (recién horneado) -> ordenado (al enfriarse)
dots = "".join(f'<circle cx="{x}" cy="{y}" r="4" class="as-svg__fill"/>' for x, y in [(40,70),(62,96),(48,120),(80,64),(92,110),(70,140),(110,84),(104,132),(54,150),(118,58)])
rows = "".join(f'<circle cx="{200+i*18}" cy="{y}" r="4" class="as-svg__fill"/>' for y in (70,92,114,136) for i in range(5))
V["c3"] = svg("A la izquierda, el almidón de la miga desordenado; a la derecha, reordenado en filas al enfriarse",
    ARROW + BG + dots + rows +
    '<line x1="140" y1="104" x2="180" y2="104" class="as-svg__ink" stroke-width="2" marker-end="url(#pan-duro-ah)"/>'
    '<text x="80" y="180" text-anchor="middle" class="as-svg__label" font-size="16">recién horneado</text>'
    '<text x="236" y="180" text-anchor="middle" class="as-svg__label" font-size="16">al enfriarse</text>'
    '<text x="160" y="30" text-anchor="middle" class="as-svg__muted" font-size="16">el almidón de la miga</text>')
V["c4"] = svg("Una miga que conserva su agua, pero igual se pone firme",
    BG + pan(100, 60) +
    '<path d="M60 70 C50 86 48 98 60 104 C72 98 70 86 60 70 Z" class="as-svg__cool"/>'
    '<text x="60" y="130" text-anchor="middle" class="as-svg__label" font-size="16">el agua</text><text x="60" y="148" text-anchor="middle" class="as-svg__label" font-size="16">se queda</text>'
    '<text x="160" y="184" text-anchor="middle" class="as-svg__label" font-size="17">y la miga igual se endurece</text>')
def thermo(x, label):
    return (f'<rect x="{x}" y="44" width="16" height="96" rx="8" class="as-svg__ink"/><circle cx="{x+8}" cy="148" r="12" class="as-svg__cool"/>'
            f'<line x1="{x+8}" y1="140" x2="{x+8}" y2="100" class="as-svg__coolline"/><text x="{x+8}" y="182" text-anchor="middle" class="as-svg__label" font-size="16">{label}</text>')
V["c5"] = svg("Un refrigerador entre 0 y 10 grados: el pan se endurece más rápido",
    BG + '<rect x="30" y="24" width="96" height="150" rx="10" class="as-svg__ink"/><line x1="30" y1="76" x2="126" y2="76" class="as-svg__ink"/>'
    '<line x1="112" y1="40" x2="112" y2="62" class="as-svg__ink"/><line x1="112" y1="92" x2="112" y2="120" class="as-svg__ink"/>' +
    pan(42, 112, 0.6) + thermo(150, "0 a 10 °C") +
    '<text x="250" y="90" text-anchor="middle" class="as-svg__label" font-size="18">más</text><text x="250" y="110" text-anchor="middle" class="as-svg__label" font-size="18">rápido</text>')
flake = "".join(f'<line x1="0" y1="0" x2="0" y2="-26" class="as-svg__coolline" transform="translate(84,96) rotate({a})"/>' for a in range(0, 360, 60))
V["c6"] = svg("Un copo de nieve y un pan: en el congelador el endurecimiento se demora más",
    BG + flake + '<circle cx="84" cy="96" r="5" class="as-svg__cool"/>' + pan(160, 70) +
    '<text x="84" y="160" text-anchor="middle" class="as-svg__label" font-size="16">congelador</text>'
    '<text x="220" y="160" text-anchor="middle" class="as-svg__label" font-size="17">se demora más</text>')
V["c8"] = svg("Un pan calentado: se ablanda por un rato, pero no vuelve a ser recién horneado",
    BG + pan(100, 90) +
    '<path d="M120 76 q-8 -12 0 -24 q8 -12 0 -24" class="as-svg__warmline"/><path d="M160 76 q-8 -12 0 -24 q8 -12 0 -24" class="as-svg__warmline"/><path d="M200 76 q-8 -12 0 -24 q8 -12 0 -24" class="as-svg__warmline"/>'
    '<text x="160" y="176" text-anchor="middle" class="as-svg__label" font-size="17">blando por un rato</text>')

L = json.load(open(os.path.join(ROOT, "data", "lessons", "pan-duro.r2.json"), encoding="utf-8"))
L["revision"] = 3
for c in L["tarjetas"]:
    if c["id"] in V: c["visual"] = V[c["id"]]
validate(L)
out = os.path.join(ROOT, "borradores", "muestra_visual"); os.makedirs(out, exist_ok=True)
open(os.path.join(out, "pan-duro.r3.json"), "w", encoding="utf-8").write(json.dumps(L, ensure_ascii=False, indent=2))
print("ok", sum(1 for c in L["tarjetas"] if "visual" in c), "ilustraciones")
