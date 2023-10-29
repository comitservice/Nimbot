# `niimprint` &mdash; Niimbot Printer Client

**Fork changelog & differences from original version:**

- Tested on Niimbot B21 and Python 3.11. Niimbot D11 support may be broken!
- Added transport abstraction: switch between bluetooth and USB (serial)
- Switched to [click](https://click.palletsprojects.com/) CLI library instead of argparse
- Integrated [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) and [poetry](https://python-poetry.org)
- Integrated [pre-commit](https://pre-commit.com/) and [ruff](https://docs.astral.sh/ruff/), re-formatted all files
- Miscellaneous refactoring / file renaming / etc.

## Installation

Recommended method is to use [poetry](https://python-poetry.org) and install with `poetry install`. However `requirements.txt` is also provided for convenience. Project is tested on Python 3.11, but should work on other versions.

## Usage

```
$ python niimprint --help

Usage: niimprint [OPTIONS]

Options:
  -m, --model [b21|d11]        Niimbot printer model  [default: b21]
  -c, --conn [usb|bluetooth]   Connection type  [default: usb]
  -a, --addr TEXT              Bluetooth MAC address OR serial device path
  -d, --density INTEGER RANGE  Print density  [default: 5; 1<=x<=5]
  -i, --image PATH             Image path  [required]
  --help                       Show this message and exit.
```

## Examples

**B21, USB connection, 30x15 mm (240x120 px) label.** On linux, you can try to omit `--addr` option and let the script to auto-detect the serial port (it will fail if there're multiple available ports). On windows, serial ports will be named like `COM1`, `COM2` etc. (check in device manager).

```
python niimprint --addr /dev/ttyACM0 --image examples/B21_30x15mm_240x120px.png
```

**B21, bluetooth connection:** untested (todo).

**D11:** completly untested, however original fork supports it. If you have D11 at hand and willing to test, please open an issue!

## Image vs Label size

### Niimbot B21

According to my observations, B21 has **8 pixels per mm** resolution. But there's one catch: printer specs say it supports up to 50mm-wide labels (which sould translate to `50 * 8 = 400` pixels). However trying to print anything larger than `384` pixels resulted in error. My guess it's the actual hardware limit, which is "almost equal" to stated 50 mm.

### Niimbot D11

???
