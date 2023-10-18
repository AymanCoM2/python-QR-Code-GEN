import qrcode
from PIL import Image

# Define the content of the QR code
data = "Don't be Good"

# Define a list of sizes and resolutions
size_and_resolution_list = [
    (90, 90, 72),  # Size: 100x100 pixels, Resolution: 72 DPI
    (100, 100, 72),  # Size: 100x100 pixels, Resolution: 72 DPI
    (200, 200, 300),  # Size: 200x200 pixels, Resolution: 300 DPI
    (300, 300, 600),  # Size: 300x300 pixels, Resolution: 600 DPI
]

# Generate QR code images with different sizes and resolutions
for size, resolution, dpi in size_and_resolution_list:
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size), Image.ANTIALIAS)
    img.save(f"qr_code_{size}x{size}_{dpi}dpi.png", dpi=(dpi, dpi))
