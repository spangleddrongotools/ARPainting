from PIL import Image

# ----- CONFIG -----
input_file = "painting.jpg"       # Your painting file
output_file = "painting_square.png"  # Output square image
background_color = (0, 0, 0)   # black padding (RGB)
# ------------------

# Open the painting image
img = Image.open(input_file)
width, height = img.size

# Determine the size of the new square image
new_size = max(width, height)

# Create a new square image with background color
new_img = Image.new("RGB", (new_size, new_size), background_color)

# Paste the original painting in the center
paste_x = (new_size - width) // 2
paste_y = (new_size - height) // 2
new_img.paste(img, (paste_x, paste_y))

# Save the square image
new_img.save(output_file)

print(f"Saved square image: {output_file}")
