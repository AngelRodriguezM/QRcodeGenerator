# QR Code Generator

A small web app that turns a URL (or any text) into a QR code. Built in Python with [ReactPy](https://reactpy.dev) for the UI and [qrcode](https://pypi.org/project/qrcode/) for generation.

## Features

- Enter a URL and generate a QR code instantly
- Preview the QR code in the browser
- Download it as a PNG
- Can also be used as a command-line tool

## Project structure

```
QRcodeGenerator/
├── app.py              # Entry point: starts the ReactPy server
├── index.py            # UI component (input, button, preview, styles)
└── python/
    └── generator.py    # generate_qr(): builds the QR code as a PNG data URI
```

## Requirements

- Python 3.9+

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/AngelRodriguezM/QRcodeGenerator
   cd QRcodeGenerator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install reactpy qrcode[pil]
   ```

4. Run the app from the project root:

   ```bash
   python app.py
   ```

5. Open the local URL printed in the terminal (usually http://127.0.0.1:8000).

## Command-line usage

You can also generate a QR code without the UI:

```bash
python python/generator.py
```

Enter a URL when prompted, and a `qrcode.png` file is saved in the current directory.

## Deployment notes

ReactPy needs a long-running Python server with WebSocket support, so static hosts like Netlify won't work. Use a host such as Render, Railway or Fly.io instead. The built-in `run()` is for development only. In production, mount the app on FastAPI and serve it with `uvicorn`.
