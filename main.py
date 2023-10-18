# $ pip install "qrcode[pil]"
import qrcode
img = qrcode.make('Dont be Good')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
# How to Replace it in a Docx ??


# 