from PIL import Image, ImageOps
import os

# Step 1: Convert the image to a silhouette
def convert_to_silhouette(image_path, output_path, threshold=128):
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    image = image.point(lambda p: p > threshold and 255)  # Apply threshold
    image = ImageOps.invert(image)  # Invert the image to get a silhouette
    image.save(output_path)
    print(f'Silhouette image saved to {output_path}')

# Step 2: Generate an SVG from the silhouette
def convert_to_svg(silhouette_path, svg_output_path):
    image = Image.open(silhouette_path)
    width, height = image.size
    svg_content = f'''<svg height="{height}" width="{width}" xmlns="http://www.w3.org/2000/svg">
<image href="{silhouette_path}" height="{height}" width="{width}"/>
</svg>'''
    with open(svg_output_path, 'w') as svg_file:
        svg_file.write(svg_content)
    print(f'SVG file saved to {svg_output_path}')

# Step 3: Generate TTF font using FontForge
def generate_ttf_font(svg_path, ttf_output_path):
    import fontforge

    # Open a new font
    font = fontforge.font()

    # Add a glyph
    glyph = font.createChar(ord('A'))  # Use Unicode code point for the glyph (e.g., 'A')
    glyph.importOutlines(svg_path)

    # Set glyph parameters
    glyph.left_side_bearing = glyph.right_side_bearing = 10
    glyph.width = 500  # Set glyph width

    # Generate TTF font
    font.generate(ttf_output_path)
    print(f'TTF font saved as {ttf_output_path}')

def main():
    # Prompt the user for the image path
    image_path = input("Enter the path to the image: ")
    silhouette_path = 'silhouette.png'  # Path to save the silhouette image
    svg_path = 'silhouette.svg'  # Path to save the SVG file
    ttf_path = 'silhouette_font.ttf'  # Path to save the TTF font

    # Convert image and generate SVG
    convert_to_silhouette(image_path, silhouette_path)
    convert_to_svg(silhouette_path, svg_path)
    
    # Generate TTF font
    generate_ttf_font(svg_path, ttf_path)

if __name__ == "__main__":
    main()
