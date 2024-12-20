import qrcode

# Create a QR code object with a specific version, box size, border, and error correction level
qr = qrcode.QRCode(
    version=3,
    box_size=20,
    border=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Define the data to be encoded in the QR code
data = "http://priyanshurathod07.wordpress.com"

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code fit the data
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("Infoframe.png")

print("QR code generated and saved as 'qr_code.png'")
