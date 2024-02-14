---
hide:
  - navigation
---

## Packet structure

Niimbot uses simple TLV packet with preamble, postamble and checksum.

Every field of packet uses big endian.

    |5555|c2|01|02|c1|aaaa|
     │    │  │  │  │  └ Postamble (constant)
     │    │  │  │  └─── Checksum (xor sum of type, length and value)
     │    │  │  └────── Value
     │    │  └───────── Length (of data)
     │    └──────────── Type
     └───────────────── Preamble (constant)

## Line encoding packets
Niimbot uses three types of packet to print image.

All three packet type has repeat count. So, repetition of same data can be reduced to one packet.

Currently niimprint's encoder only uses line packet without optimization.

_(Common packet fields are omitted for clarity.)_

### Blank packet
Blank packet (packet type 0x84) encodes blank line.

    |5555|84|03|0000|0a|8d|aaaa|
                │    └ Repeat count
                └───── Line count

This packet will print 10 blank lines.

### Line packet
line packet (packet type 0x85) encodes line as bitmap.

    |5555|85|12|000a|00|01|0f|02|0000000000000001fffe0000|91|aaaa
                │    │  │  │  │  └ Bitmap data
                │    │  │  │  └─── Repeat count
                │    │  │  └────── Pixel count (right)  (bit count of 0x00000000)
                │    │  └───────── Pixel count (middle) (bit count of 0x00000001)
                │    └──────────── Pixel count (left)   (bit count of 0xfffe0000)
                └───────────────── Line count

This packet will print 2 bitmap lines.

### Points packet
points packet (packet type 0x83) encodes line as array of 1D points.

    5555|83|0e|000c|00|01|03|07|003f0040004d004e|f8|aaaa|
                │    │  │  │  │  └ Point data (0x003f, 0x0040, 0x004d, 0x004e)
                │    │  │  │  └─── Repeat count
                │    │  │  └────── Pixel count (right)
                │    │  └───────── Pixel count (middle)
                │    └──────────── Pixel count (left)
                └───────────────── Line count

This packet will print 7 lines with points.

### Todo

!!! question

    How does B21 encodes more then 96 pixels? 
