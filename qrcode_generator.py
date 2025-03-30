import qrcode

# Data to be encoded in QR code
data = "i am pratiksha shete"

#in data ypu can add you git hub link or any text


# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each box in the QR code grid
    border=4  # Border thickness
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate and save the QR code image
qr_image = qr.make_image(fill="black", back_color="white")
qr_image.save("qr_code.png")

print("QR Code generated and saved as 'qr_code.png'")
