import pyqrcode
import png

from pyqrcode import QRCode
# La url que quiero que se imprima en el QR
s = "https://www.inacap.cl"
# Generar el QR
url = pyqrcode.create(s) # la variable s es la URL

# Crea y guarda un archivo SVG con el nombre "URLINACAP.svg"
url.svg("URLINACAP.svg", scale = 8)

# Crea y guarda el archivo png con el nombre "URLINACAP.png"
url.png('URLINACAP.png', scale = 6)