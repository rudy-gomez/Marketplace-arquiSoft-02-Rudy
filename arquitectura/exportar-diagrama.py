"""Genera una lámina SVG blanca para Markdown desde el HTML de Archify."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

folder = Path(__file__).resolve().parent
html = (folder / 'marketplace-mascotas.html').read_text(encoding='utf-8')
svg = re.search(r'<svg\s+viewBox="0 0 1120 620".*?</svg>', html, re.S).group()
inner = svg[svg.index('>') + 1:svg.rfind('</svg>')]
variables = re.search(r'\[data-theme="light"\]\s*\{([^}]+)\}', html).group(1)
rules = re.findall(r'\.(?:c|t|a|m)-[\w-]+\s*\{[^}]+\}', html)
css = ':root {' + variables + '}\n' + '\n'.join(rules)
css += '\ntext { font-family: Arial, Helvetica, sans-serif; }'
css += '\n.semantic-sigil { fill: none; stroke: currentColor; stroke-width: 1.35; stroke-linecap: round; stroke-linejoin: round; }'
for kind in ('frontend', 'backend', 'database', 'external'):
    css += f'\n.semantic-sigil-{kind} {{ color: var(--{kind}-stroke); }}'
output = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="720" viewBox="0 0 1160 720" role="img" aria-labelledby="sheet-title sheet-desc">
<title id="sheet-title">Arquitectura del Marketplace de mascotas</title>
<desc id="sheet-desc">Actores, presentación, lógica de negocio y datos. Pedidos se integra con la pasarela de pago, ERP y servicio de envío.</desc>
<style>{css}</style>
<rect width="1160" height="720" fill="#ffffff"/>
<rect x="1" y="1" width="1158" height="718" rx="18" fill="#ffffff" stroke="#d9e2ec" stroke-width="2"/>
<rect x="25" y="25" width="5" height="28" rx="2.5" fill="#0891b2"/>
<text x="43" y="43" font-size="21" font-weight="700" fill="#0f172a">Marketplace de mascotas</text>
<text x="1134" y="41" text-anchor="end" font-size="11" letter-spacing="1.2" fill="#64748b">ARQUITECTURA DEL SISTEMA</text>
<path d="M 25 66 H 1135" stroke="#e2e8f0"/>
<g transform="translate(20 80)">{inner}</g>
</svg>'''
ET.fromstring(output)
(folder / 'marketplace-mascotas-blanco.svg').write_text(output, encoding='utf-8')
print('SVG generado y XML verificado.')
