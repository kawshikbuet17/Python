import qrcode
from PIL import Image
qr = qrcode.make('Hello Kawshik. This is a qr code')
# qr.save('qr_code_generator/myqr.png')
qr.show()