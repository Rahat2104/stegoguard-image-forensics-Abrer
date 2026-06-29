from pathlib import Path
import struct
import zlib

mode = Path("lab_mode.txt").read_text(encoding="utf-8").strip().lower()

if mode not in ["clean", "suspicious"]:
    raise SystemExit("lab_mode.txt must contain either: clean or suspicious")

Path("images").mkdir(exist_ok=True)

WIDTH = 800
HEIGHT = 400


def png_chunk(chunk_type, data):
    return (
        struct.pack(">I", len(data))
        + chunk_type
        + data
        + struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
    )


def create_large_png(width, height):
    raw_data = bytearray()

    for y in range(height):
        raw_data.append(0)

        for x in range(width):
            red = int(40 + (x / width) * 160)
            green = int(80 + (y / height) * 120)
            blue = 200

            raw_data.extend([red, green, blue])

    png_signature = b"\x89PNG\r\n\x1a\n"

    ihdr = struct.pack(
        ">IIBBBBB",
        width,
        height,
        8,
        2,
        0,
        0,
        0,
    )

    png_data = (
        png_signature
        + png_chunk(b"IHDR", ihdr)
        + png_chunk(b"IDAT", zlib.compress(bytes(raw_data)))
        + png_chunk(b"IEND", b"")
    )

    return png_data


png_data = create_large_png(WIDTH, HEIGHT)

if mode == "suspicious":
    png_data += b"\nCONFIDENTIAL: This is harmless demo hidden data for the StegoGuard lab.\n"

Path("images/student_image.png").write_bytes(png_data)

print(f"Created images/student_image.png in {mode} mode")
print(f"Image size: {WIDTH}x{HEIGHT} pixels")
