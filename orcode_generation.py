import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = input("Enter the website: ")

# Generate QR code
url = pyqrcode.create(s)

# Create and save the QR code
url.svg("mydy.svg", scale = 8)
