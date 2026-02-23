# Image-Resizer-Tool

The Image Resizer Tool is a Python-based application designed to resize multiple images automatically. It processes images from an input folder, resizes them to specified dimensions, and saves the resized images in an output folder. This tool helps automate image resizing efficiently. It helps reduce manual effort and improves efficiency when working with multiple images.

Features
	•	Resize multiple images at once
	•	Supports JPG, JPEG, and PNG formats
	•	Automatically creates output folder
	•	Simple and easy to use

Technologies Used
	•	Python
	•	Pillow (PIL) library
	•	VS Code

How to Use
	1.	Place images in the input_images folder.
	2.	Run the input_images.py file.
	3.	Resized images will be saved in output_images folder.
 
Objective

The main objective of this project is to automate the process of resizing images using Python and the Pillow library. It demonstrates file handling, folder management, and image processing concepts.

Features
	•	Batch processing of multiple images
	•	Supports JPG, JPEG, and PNG formats
	•	Automatic creation of output folder if not available
	•	Maintains original image names
	•	Fast and efficient processing
	•	Easy to use and modify

Technologies Used
	•	Programming Language: Python
	•	Library: Pillow (PIL)
	•	Development Tool: Visual Studio Code
	•	Operating System: Windows

Project Structure

Image-Resizer-Tool/
│
├── input_images/        # Folder containing original images
├── output_images/       # Folder containing resized images
├── image_resizer.py     # Main Python script
└── README.md            # Project documentation

How It Works

The script reads all image files from the input_images folder. It checks for supported image formats and resizes each image to the specified width and height using the Pillow library. The resized images are then saved in the output_images folder.

Installation
	1.	Install Python (version 3.x recommended)
	2.	Install Pillow library using command:

pip install pillow

	3.	Download or clone this repository

Usage
	1.	Place images inside the input_images folder
	2.	Open the project folder in VS Code
	3.	Run the image_resizer.py script
	4.	Check the resized images in output_images folder

Expected Output

All images from the input_images folder will be resized and saved in the output_images folder with the specified dimensions.

Applications
	•	Image preprocessing
	•	Website image optimization
	•	Reducing image file size
	•	Preparing images for projects and presentations

Author

Likitha Manchikanti

License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

