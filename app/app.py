from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import qrcode

app = FastAPI()


@app.get("/qr")
def main(deep_link, qr_color="White", bg_color="Black", format="png", logo=False):
    def iterfile(url: str, QRcolor, BGcolor):
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        QRcode.add_data(url)
        QRcode.make()

        im_png = QRcode.make_image(fill_color=QRcolor, back_color=BGcolor)
        im_png.save(f"qr_code.{format}")
        some_file_path = f"qr_code.{format}"
        with open(some_file_path, mode='rb') as file_like:
            yield from file_like
        
    return StreamingResponse(iterfile(url=deep_link, QRcolor=qr_color, BGcolor=bg_color), media_type=f"image/{format}")

