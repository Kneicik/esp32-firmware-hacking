import subprocess
import re

INPUT_BIN = "firmware_only.bin"
OUTPUT_BIN = "firmware_trimmed.bin"

def dump_firmware_from_device(output_path):
    print("[*] Starting firmware dump from the device...")
    result = subprocess.run(
        ["esptool.py", "--chip", "esp32s3", "--port", "/dev/cu.wchusbserial595B0150521", "read_flash", "0x10000", "0x400000", output_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    if result.returncode != 0:
        raise RuntimeError(f"[!] Error during firmware dump: {result.stdout}")
    
    print(f"[+] Firmware dumped to {output_path}")

def get_hash_from_image_info(bin_file):
    result = subprocess.run(
        ["esptool.py", "--chip", "esp32s3", "image_info", bin_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    match = re.search(r"Validation Hash:\s*([a-f0-9]+)", result.stdout)
    if not match:
        raise RuntimeError("Hash not found in esptool output.")
    
    hash_value = match.group(1)
    print(f"[*] Hash found: {hash_value}")
    return hash_value

def trim_file_after_hash(input_path, output_path, hash_value):
    with open(input_path, "rb") as f:
        data = bytearray(f.read())

    hash_bytes = bytes.fromhex(hash_value)
    
    hash_position = data.rfind(hash_bytes)
    
    if hash_position == -1:
        raise RuntimeError("Hash not found in the file.")
    
    print(f"[*] Removing data after the hash (hash at position {hash_position})")
    trimmed_data = data[:hash_position]

    with open(output_path, "wb") as f:
        f.write(trimmed_data + hash_bytes)

    print(f"[+] Trimmed file saved: {output_path}")

if __name__ == "__main__":
    dump_firmware_from_device(INPUT_BIN)
    hash_value = get_hash_from_image_info(INPUT_BIN)
    trim_file_after_hash(INPUT_BIN, OUTPUT_BIN, hash_value)
