# $ pip install "qrcode[pil]"
import qrcode
img = qrcode.make('Ayman Salah')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")