"""QR Code Generator — creates a QR code image from a URL."""

import argparse
import logging
import os

import qrcode

LOG_DIR = os.getenv("LOG_DIR", "logs")
QR_DIR = os.getenv("QR_CODE_DIR", "qr_codes")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(QR_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def generate_qr_code(url: str, filename: str = "qr_code.png") -> str:
    """Generate a QR code for the given URL and save it to the QR directory."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    output_path = os.path.join(QR_DIR, filename)
    img.save(output_path)

    logging.info("Generated QR code for %s at %s", url, output_path)
    return output_path


def main():
    """Parse arguments and generate the QR code."""
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument(
        "--url",
        default="https://github.com/kaw393939",
        help="The URL to encode in the QR code.",
    )
    args = parser.parse_args()

    path = generate_qr_code(args.url)
    print(f"QR code generated for {args.url}")
    print(f"Saved to {path}")


if __name__ == "__main__":
    main()  # pragma: no cover