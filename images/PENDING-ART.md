# 🎨 Ilustraciones Pendientes

**Problema:** La cuenta de OpenAI alcanzó el límite de facturación.
**Solución:** Agregar créditos en https://platform.openai.com/settings/organization/billing

## Cuando esté resuelto, ejecutar:

```bash
cd ~/clawd/storybook/el-club-de-los-inventores/webapp/images

# Estilo artístico (usar como prefijo en todos los prompts):
STYLE="Whimsical watercolor children's book illustration, warm inviting colors, expressive characters, Studio Ghibli meets Quentin Blake style, for ages 8-10"

# Generar cada imagen:
python3 /home/ubuntu/.npm-global/lib/node_modules/clawdbot/skills/openai-image-gen/scripts/gen.py \
  --model dall-e-3 --quality hd --size 1792x1024 --style vivid --out-dir . \
  --prompt "$STYLE. Cover: Two kids (boy and girl, 10yo) discovering old leather notebook with glowing light, inventor workshop silhouette background"

# Repetir para cada capítulo cambiando el prompt...
```

## Prompts listos para cada imagen:

1. **cover.png** - Cover: Two kids discovering old leather notebook with mysterious glow
2. **ch01.png** - Rainy day discovery: Kids excited looking at old notebook with maps and drawings
3. **ch02a.png** - Mysterious basement with old machinery, cobwebs, faint light through window
4. **ch02b.png** - Garden at dusk with strange flickering lights, old windmill in background  
5. **ch03a.png** - Grandfather's workshop full of inventions and tools, warm lighting
6. **ch03b.png** - Kids helping each other climb through difficult window, teamwork
7. **ch03c.png** - Kids building first invention with recycled materials, concentration
8. **ch03d.png** - Kids with notebooks observing lights, taking scientific notes
9. **ch05a.png** - Secret underground laboratory reveal, wonder on kids' faces, machines everywhere
10. **final.png** - Kids as "neighborhood inventors" helping community, proud moment

## Script completo de generación:

```bash
#!/bin/bash
STYLE="Whimsical watercolor children's book illustration, warm colors, expressive characters, Studio Ghibli meets Quentin Blake, ages 8-10"
OUT="~/clawd/storybook/el-club-de-los-inventores/webapp/images"
GEN="python3 /home/ubuntu/.npm-global/lib/node_modules/clawdbot/skills/openai-image-gen/scripts/gen.py --model dall-e-3 --quality hd --size 1792x1024 --style vivid --out-dir $OUT"

$GEN --prompt "$STYLE. Book cover: Two curious kids (10yo boy and girl) holding glowing old leather notebook, inventor silhouettes in background"
mv $OUT/*.png $OUT/cover.png

$GEN --prompt "$STYLE. Chapter 1: Rainy Saturday, two kids excited discovering old notebook with strange drawings and maps"
mv $OUT/*.png $OUT/ch01.png

$GEN --prompt "$STYLE. Mysterious abandoned basement, old machinery covered in dust, cobwebs, single beam of light"
mv $OUT/*.png $OUT/ch02a.png

$GEN --prompt "$STYLE. Garden at twilight, strange flickering lights in distance, old windmill silhouette, two kids watching"
mv $OUT/*.png $OUT/ch02b.png

$GEN --prompt "$STYLE. Cozy grandfather workshop, shelves full of inventions and tools, warm lamp light, nostalgic"
mv $OUT/*.png $OUT/ch03a.png

$GEN --prompt "$STYLE. Two kids helping each other climb through small window, teamwork moment, determination"
mv $OUT/*.png $OUT/ch03b.png

$GEN --prompt "$STYLE. Kids building invention with recycled materials bottles cardboard, focused creative work"
mv $OUT/*.png $OUT/ch03c.png

$GEN --prompt "$STYLE. Kids sitting in grass with notebooks, observing mysterious lights, scientific curiosity"
mv $OUT/*.png $OUT/ch03d.png

$GEN --prompt "$STYLE. Secret underground laboratory reveal moment, kids amazed, vintage machines and inventions everywhere"
mv $OUT/*.png $OUT/ch05a.png

$GEN --prompt "$STYLE. Happy ending: kids as neighborhood inventors helping community, proud moment, people thanking them"
mv $OUT/*.png $OUT/final.png

echo "✅ All images generated!"
```
