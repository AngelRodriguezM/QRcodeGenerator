from reactpy import html, component, use_state

from python.generator import generate_qr


STYLES = """
body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f1f5f9;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    color: #0f172a;
}
.card {
    width: 100%;
    max-width: 380px;
    margin: 16px;
    padding: 32px;
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
    text-align: center;
}
.title {
    margin: 0 0 4px;
    font-size: 24px;
}
.subtitle {
    margin: 0 0 24px;
    color: #64748b;
    font-size: 14px;
}
.form {
    display: flex;
    gap: 8px;
}
.input {
    flex: 1;
    min-width: 0;
    padding: 10px 12px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 14px;
    outline: none;
}
.input:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}
.button {
    padding: 10px 16px;
    border: none;
    border-radius: 8px;
    background: #2563eb;
    color: #ffffff;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
}
.button:hover {
    background: #1d4ed8;
}
.error {
    margin: 12px 0 0;
    color: #dc2626;
    font-size: 13px;
}
.result {
    margin-top: 24px;
    padding-top: 24px;
    border-top: 1px solid #e2e8f0;
}
.qr {
    width: 220px;
    height: 220px;
    image-rendering: pixelated;
}
.download {
    display: inline-block;
    margin-top: 12px;
    padding: 8px 16px;
    border: 1px solid #2563eb;
    border-radius: 8px;
    color: #2563eb;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
}
.download:hover {
    background: #eff6ff;
}
"""


@component
def indexApp():
    url, set_url = use_state("")
    qr_src, set_qr_src = use_state(None)
    error, set_error = use_state(None)

    def handle_change(event):
        set_url(event["target"]["value"])

    def handle_generate(event):
        value = url.strip()
        if not value:
            set_error("Please enter a URL.")
            set_qr_src(None)
            return
        set_error(None)
        set_qr_src(generate_qr(value))

    return html.div(
        html.style(STYLES),
        html.div(
            {"class_name": "card"},
            html.h2({"class_name": "title"}, "QR Code Generator"),
            html.p({"class_name": "subtitle"}, "Paste a link to turn it into a QR code."),
            html.div(
                {"class_name": "form"},
                html.input(
                    {
                        "class_name": "input",
                        "type": "text",
                        "placeholder": "https://example.com",
                        "value": url,
                        "on_change": handle_change,
                    }
                ),
                html.button(
                    {"class_name": "button", "on_click": handle_generate},
                    "Generate",
                ),
            ),
            html.p({"class_name": "error"}, error) if error else "",
            html.div(
                {"class_name": "result"},
                html.img({"class_name": "qr", "src": qr_src, "alt": "QR code"}),
                html.br(),
                html.a(
                    {"class_name": "download", "href": qr_src, "download": "qrcode.png"},
                    "Download PNG",
                ),
            )
            if qr_src
            else "",
        ),
    )
