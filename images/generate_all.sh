#!/bin/bash
cd ~/clawd/storybook/el-club-de-los-inventores/webapp/images

STYLE="Whimsical watercolor children's book illustration, warm inviting colors, expressive characters, Studio Ghibli meets Quentin Blake style, for kids ages 8-10"

generate_image() {
    local name=$1
    local prompt=$2
    echo "🎨 Generando: $name..."
    
    response=$(curl -s https://api.openai.com/v1/images/generations \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -H "Content-Type: application/json" \
      -d "{
        \"model\": \"dall-e-3\",
        \"prompt\": \"$STYLE. $prompt\",
        \"n\": 1,
        \"size\": \"1792x1024\",
        \"quality\": \"hd\"
      }")
    
    url=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',[{}])[0].get('url',''))" 2>/dev/null)
    
    if [ -n "$url" ] && [ "$url" != "None" ]; then
        curl -s "$url" -o "${name}.png"
        echo "✅ ${name}.png"
    else
        echo "❌ Error: $response"
    fi
}

# Chapter 1
generate_image "ch01" "Rainy Saturday morning, two excited kids discovering an old mysterious notebook with strange drawings and maps inside, rain on window, warm indoor lighting"

# Chapter 2A
generate_image "ch02a" "Mysterious abandoned basement entrance with old rusty metal door, overgrown bushes, cobwebs, faint mysterious light coming from below, two kids approaching cautiously"

# Chapter 2B  
generate_image "ch02b" "Old windmill at twilight with strange green flickering lights coming from windows, two kids watching from a field, magical mysterious atmosphere"

# Chapter 3A
generate_image "ch03a" "Cozy grandfather workshop full of vintage inventions and tools, warm lamp light, shelves with gears and old machines, nostalgic feeling"

# Chapter 3B
generate_image "ch03b" "Two kids helping each other climb through a small basement window, teamwork moment, determination on their faces"

# Chapter 3C
generate_image "ch03c" "Kids building their first invention with recycled materials like bottles cardboard and wires, focused creative work, messy but exciting"

# Chapter 3D
generate_image "ch03d" "Two kids sitting in grass with notebooks, carefully observing and documenting mysterious lights in the distance, scientific curiosity"

# Chapter 5A
generate_image "ch05a" "Secret underground laboratory reveal, two kids amazed looking at a huge copper and glass machine with blue glowing cables, steampunk inventor aesthetic"

# Final
generate_image "final" "Happy ending scene: group of neighborhood kids as proud young inventors helping community, building solar lamps and gadgets, joyful celebration"

echo ""
echo "🎉 ¡Todas las imágenes generadas!"
ls -la *.png 2>/dev/null | wc -l
