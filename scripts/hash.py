import subprocess
import re
import hashlib

INPUT_BIN = "firmware_trimmed.bin"
OUTPUT_BIN = "firmware_fixed.bin"

def get_calculated_checksum(bin_file):
    result = subprocess.run(
        ["esptool.py", "--chip", "esp32s3", "image_info", bin_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    match = re.search(r"calculated ([0-9a-fx]+)", result.stdout)
    if not match:
        raise RuntimeError("Checksum not found in esptool output.")
    return int(match.group(1), 16)

def patch_checksum_and_hash(in_path, out_path, checksum):
    with open(in_path, "rb") as f:
        data = bytearray(f.read())

    if len(data) % 16 == 0:
        print("[*] Removing old SHA256...")
        data = data[:-32]

    print(f"[*] Writing checksum: 0x{checksum:02x}")
    data[-1] = checksum

    print("[*] Calculating SHA256...")
    sha256 = hashlib.sha256(data).digest()

    data += sha256

    with open(out_path, "wb") as f:
        f.write(data)

    print(f"SHA256: {sha256.hex()}")
    print(f"[+] Saved: {out_path}")

if __name__ == "__main__":
    chk = get_calculated_checksum(INPUT_BIN)
    patch_checksum_and_hash(INPUT_BIN, OUTPUT_BIN, chk)
