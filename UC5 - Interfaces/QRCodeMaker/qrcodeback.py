import qrcode
from PIL import Image, ImageDraw
from pathlib import Path
class gerador_qr_code():
    def __init__(self):
        self.nothing = 0
        self.path = Path.cwd()
        
    def gerar_qrcode(self, url):
        if len(url) == 0:
            return False
        if url.startswith("https://"):
            qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save(f"{self.path}/qrExport.png")
            return True
        if url.startswith("www."):
            url = f'https://{url}'
            qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save(f"{self.path}/qrExport.png")
            return True
        else:
            return False