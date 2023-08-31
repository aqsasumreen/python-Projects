import sys

import qrcode
# from PIL import image
#
qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=8, border=10)
# qr.add_data('https://www.youtube.com/@CodeWithHarry')
qr.add_data('https://www.youtube.com/@CodeWithHarry')
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("third_qr.png")
print(sys.executable)