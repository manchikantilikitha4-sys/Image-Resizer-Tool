import os
from PIL import Image

# Input and Output folders
input_folder = "input_images"
output_folder = "output_images"

# Resize dimensions
new_width = 800
new_height = 600

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize image
        resized_img = img.resize((new_width, new_height))

        # Save resized image in output folder
        output_path = os.path.join(output_folder, filename)
        resized_img.save(output_path)

        print(f"{filename} resized and saved successfully.")

print("All images processed successfully.")