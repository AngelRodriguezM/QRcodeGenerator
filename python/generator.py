import base64
import io

import qrcode


def generate_qr(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


if __name__ == "__main__":
    url = input("Enter Url: ").strip()

    file_path = "qrcode.png"

    qr = qrcode.QRCode()
    qr.add_data(url)

    img = qr.make_image()

    img.save(file_path)

    print("qr code generated")
