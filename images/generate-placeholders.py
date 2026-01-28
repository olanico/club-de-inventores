#!/usr/bin/env python3
"""Generate SVG placeholder images for the storybook"""

import os

placeholders = [
    ("cover", "📚 El Club de los Inventores", "#4A90D9"),
    ("ch01", "Cap 1: El Descubrimiento", "#6B8E23"),
    ("ch02a", "Cap 2A: El Sótano Misterioso", "#8B4513"),
    ("ch02b", "Cap 2B: Luces en la Noche", "#483D8B"),
    ("ch03a", "Cap 3A: La Búsqueda", "#CD853F"),
    ("ch03b", "Cap 3B: El Camino Difícil", "#708090"),
    ("ch03c", "Cap 3C: El Primer Invento", "#20B2AA"),
    ("ch03d", "Cap 3D: El Método Científico", "#9370DB"),
    ("ch04a", "Cap 4A: Secretos del Abuelo", "#DAA520"),
    ("ch05a", "Cap 5A: El Laboratorio Secreto", "#DC143C"),
    ("final", "Final: Inventores del Barrio", "#228B22"),
]

svg_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color_dark};stop-opacity:1" />
    </linearGradient>
    <pattern id="dots" patternUnits="userSpaceOnUse" width="20" height="20">
      <circle cx="10" cy="10" r="1.5" fill="rgba(255,255,255,0.1)"/>
    </pattern>
  </defs>
  <rect width="800" height="450" fill="url(#bg)"/>
  <rect width="800" height="450" fill="url(#dots)"/>
  <text x="400" y="200" text-anchor="middle" font-family="Georgia, serif" font-size="32" fill="white" opacity="0.9">{title}</text>
  <text x="400" y="260" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="white" opacity="0.6">🎨 Ilustración pendiente</text>
  <rect x="50" y="380" width="700" height="4" rx="2" fill="rgba(255,255,255,0.2)"/>
</svg>'''

def darken(hex_color):
    """Darken a hex color by 30%"""
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    darker = tuple(int(c * 0.7) for c in rgb)
    return '#{:02x}{:02x}{:02x}'.format(*darker)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
script_dir = os.path.dirname(os.path.abspath(__file__))

for name, title, color in placeholders:
    svg = svg_template.format(
        color=color,
        color_dark=darken(color),
        title=title
    )
    filepath = os.path.join(script_dir, f"{name}.svg")
    with open(filepath, 'w') as f:
        f.write(svg)
    print(f"✓ Created {name}.svg")

print(f"\n✅ Generated {len(placeholders)} placeholder images")
