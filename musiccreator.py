import turtle
import numpy as np
from PIL import Image, ImageDraw, ImageGrab

# Set up Turtle
t = turtle.Turtle()
t.speed(0)

# Generate a shape with Turtle
t.circle(50)

# Generate a logical pattern with NumPy
pattern = np.zeros((100, 100))
pattern[::2, ::2] = 1  # Checkerboard pattern

# Convert the pattern to an image
pattern_img = Image.fromarray(pattern)

# Capture the Turtle screen image
img_turtle = ImageGrab.grab(bbox=(50, 50, 200, 200))

# Combine the shape and pattern images
img = Image.new('RGB', (200, 200), 'white')
img.paste(pattern_img, (50, 50))
img.paste(img_turtle, (50, 50))

# Save the image
img.save('image_generator.png')