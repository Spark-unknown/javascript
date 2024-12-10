from PIL import Image

# Define ASCII characters for different grayscale levels
ASCII_CHARS = "@%#*+=-:. "

# Function to resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to convert the image to grayscale
def grayscale_image(image):
    return image.convert("L")

# Function to map grayscale values to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 32]
    return ascii_str

# Function to convert image to ASCII art
def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)
    
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    return ascii_img

# Provide the path to your image
image_path = "batman.jpg"
ascii_art = image_to_ascii(image_path)

# Print the ASCII art
print(ascii_art)

# Optionally, save the ASCII art to a text file
with open("ascii_art.txt", "w") as f:
    f.write(ascii_art)
