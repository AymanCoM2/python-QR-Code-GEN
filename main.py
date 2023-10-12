# $ pip install "qrcode[pil]"
import qrcode
img = qrcode.make('Dont be an Asshole')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
