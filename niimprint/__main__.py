import re

import click
from PIL import Image

from niimprint import BluetoothTransport, PrinterClient, SerialTransport


@click.command("print")
@click.option(
    "-m",
    "--model",
    type=click.Choice(["b21", "d11"], False),
    default="b21",
    show_default=True,
    help="Niimbot printer model",
)
@click.option(
    "-c",
    "--conn",
    type=click.Choice(["usb", "bluetooth"]),
    default="usb",
    show_default=True,
    help="Connection type",
)
@click.option(
    "-a",
    "--addr",
    help="Bluetooth MAC address OR serial device path",
)
@click.option(
    "-d",
    "--density",
    type=click.IntRange(1, 5),
    default=5,
    show_default=True,
    help="Print density",
)
@click.option(
    "-i",
    "--image",
    type=click.Path(exists=True),
    required=True,
    help="Image path",
)
def print_cmd(model, conn, addr, density, image):
    assert model != "d11", "D11 support may be broken (test yourself)"
    assert conn != "bluetooth", "Bluetooth support may be broken (test yourself)"

    if conn == "bluetooth":
        addr = addr.upper()
        assert re.fullmatch(r"([0-9A-F]{2}:){5}([0-9A-F]{2})", addr), "Bad MAC address"
        transport = BluetoothTransport(addr)
    if conn == "usb":
        port = addr if addr is not None else "auto"
        transport = SerialTransport(port=port)

    if model == "b21":
        # This may be wrong, but B21 doesn't accept anything larger. It's just shy of
        # 50mm * 8 px/mm = 400px (for vertical space it's always 8 px/mm), so lgtm.
        max_height_px = 384
    if model == "d11":
        max_height_px = 100  # I don't have D11 to test

    # Image is printed left-to-right. Generally, we expect image width to be larger
    # than image height, because that's the usual sticker aspect ratio.
    image = Image.open(image)
    assert image.width > image.height, "Are you sure image rotation is right?"
    assert image.height <= max_height_px, f"Image height too big for {model}"

    printer = PrinterClient(transport)
    printer.print_image(image, density=density)


if __name__ == "__main__":
    print_cmd()
