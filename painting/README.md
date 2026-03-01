## 🎨 Hirst-Style Spot Painting Generator
A Python project that uses the turtle graphics library and the colorgram package to recreate the iconic "Spot Painting" style of artist Damien Hirst. The script generates a 10x10 grid of randomly colored dots to create a unique piece of digital art every time it runs.

## 🚀 Features
**Color Extraction:**
Includes logic to extract a color palette from any image (e.g., images.png) using the colorgram library.Automated Painting: Uses a "snake" movement pattern to efficiently fill the canvas.Randomization: Pulls from a curated list of RGB values to ensure an aesthetically pleasing, yet random, distribution of colors.Adjustable Speed: Set to fastest to watch the artwork materialize in seconds.

## 🛠️ Installation
**Clone the repository:**
Bash
git clone https://github.com/jiya-patel2/painting.git 

Install dependencies:This project requires the colorgram.py library if you wish to extract colors from your own images.

Bash 
pip install colorgram.py 

## 💻 How It WorksThe script follows a coordinate-based logic to navigate the "canvas":
Setup:
The turtle is moved to the bottom-left corner ($x: -300, y: -300$ approx) using setheading(225) and forward(300).
Movement Logic:left(): Draws 10 dots while moving horizontally, then shifts the turtle up and turns it around.
right(): Draws 10 dots while moving back in the opposite direction.
The Grid: A loop executes these functions 5 times to produce a perfect 100-dot grid.

## 🎨 Customization
You can change the color palette by modifying the colors list in the script. The turtle uses RGB 255 mode, so each color should be a tuple:
Pythoncolors = [
    (236, 225, 81), # Vibrant Yellow
    (202, 6, 72),   # Deep Red
    (31, 188, 108), # Emerald Green
]

To extract colors from your own image, uncomment the colorgram section at the top of the script and provide a path to your image file.