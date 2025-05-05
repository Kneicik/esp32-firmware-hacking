import subprocess
import re

# Parametry plików
INPUT_BIN = "firmware_only.bin"
OUTPUT_BIN = "firmware_trimmed.bin"

# Funkcja do pobrania firmware z urządzenia
def dump_firmware_from_device(output_path):
    print("[*] Zaczynam zgrywanie firmware z urządzenia...")
    result = subprocess.run(
        ["esptool.py", "--chip", "esp32s3", "--port", "/dev/cu.wchusbserial595B0150521", "read_flash", "0x10000", "0x400000", output_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Sprawdzamy czy zrzut się udał
    if result.returncode != 0:
        raise RuntimeError(f"[!] Błąd podczas zgrywania firmware: {result.stdout}")
    
    print(f"[+] Zgrano firmware do {output_path}")

# Funkcja do pobrania hash'a z pliku za pomocą esptool
def get_hash_from_image_info(bin_file):
    result = subprocess.run(
        ["esptool.py", "--chip", "esp32s3", "image_info", bin_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Szukamy hash'a w wyniku
    match = re.search(r"Validation Hash:\s*([a-f0-9]+)", result.stdout)
    if not match:
        raise RuntimeError("Nie znaleziono hasha w wyniku esptool.")
    
    # Wyciągamy hash
    hash_value = match.group(1)
    print(f"[*] Hash znaleziony: {hash_value}")
    return hash_value

# Funkcja do przycięcia pliku po hash'u
def trim_file_after_hash(input_path, output_path, hash_value):
    with open(input_path, "rb") as f:
        data = bytearray(f.read())

    # Hash jest 32-bajtowy (64 znaki hex)
    hash_bytes = bytes.fromhex(hash_value)
    
    # Znajdź pozycję hasha w pliku
    hash_position = data.rfind(hash_bytes)
    
    if hash_position == -1:
        raise RuntimeError("Hash nie został znaleziony w pliku.")
    
    # Zapisz dane tylko przed hashem
    print(f"[*] Usuwam dane po hashie (hash na pozycji {hash_position})")
    trimmed_data = data[:hash_position]

    # Zapisz do nowego pliku
    with open(output_path, "wb") as f:
        f.write(trimmed_data + hash_bytes)  # Zostawiamy hash w pliku

    print(f"[+] Zapisano obcięty plik: {output_path}")

if __name__ == "__main__":
    # Krok 1: Zgraj firmware z urządzenia (zaktualizuj port, jeśli trzeba)
    dump_firmware_from_device(INPUT_BIN)
    
    # Krok 2: Weź hash z image_info
    hash_value = get_hash_from_image_info(INPUT_BIN)
    
    # Krok 3: Przytnij plik binarny
    trim_file_after_hash(INPUT_BIN, OUTPUT_BIN, hash_value)
