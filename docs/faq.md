---
hide:
  - navigation
---

## Image orientation

Generally, the image comes out of the printer with the same orientation you see it on your screen.
You can have your input image rotated as you like, but adjust its orientation by passing `-r <...>` flag.

See the image below for clarification.

[![](./img/image_orientation.png)]()

<!-- Excalidraw link: https://excalidraw.com/#json=vYHMBohMn5GeB-5M6SNch,TsxRmh_WKUfzYjL183FGfg -->

## Image resolution

As far as we've tested, Niimbot printers have **8 pixels per mm** (~203 dpi) resolution. The CLI prints the image you provided as-is, without any checks of the actual label size, so be careful. However the script will check if the image width is too big for selected printer. The maximum width in pixels is usually slightly less than specified maximum width in mm:

- **B21, B1, B18**: max 384 pixels (almost equal to 50 mm * 8 px/mm = 400)
- **D11**: max 96 pixels (almost equal to 15 mm * 8 px/mm = 120)
