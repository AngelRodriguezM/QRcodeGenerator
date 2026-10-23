from reactpy import html, component, use_state

from python.generator import generate_qr


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
        html.h2("QR Code Generator"),
        html.input(
            {
                "type": "text",
                "placeholder": "Enter URL",
                "value": url,
                "on_change": handle_change,
            }
        ),
        html.button({"on_click": handle_generate}, "Generate"),
        html.p({"style": {"color": "red"}}, error) if error else "",
        html.div(
            html.img({"src": qr_src, "alt": "QR code"}),
            html.br(),
            html.a({"href": qr_src, "download": "qrcode.png"}, "Download"),
        )
        if qr_src
        else "",
    )
