"""QR payloads for moving keys and signatures across an air gap.

Payloads are text with an SGDK1: prefix so they survive phone cameras and
printers. The Android demo renders them with zxing; this module only
encodes and decodes the payload format.
"""

