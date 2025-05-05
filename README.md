# ESP32 Firmware Hacking

This repository contains tools and scripts for dumping, analyzing, editing, and revalidating firmware for ESP32 devices. The project is designed to work with the ESP32-S3 chip and uses PlatformIO for building and debugging.

## Repository Structure

```
.
├── .gitignore                # Git ignore rules
├── platformio.ini            # PlatformIO configuration file
├── .pio/                     # PlatformIO build artifacts (ignored by Git)
├── decomp/                   # Decompiled firmware analysis files
├── libdeps/                  # PlatformIO library dependencies
├── scripts/                  # Python scripts for firmware manipulation
├── src/                      # Source code for PlatformIO project
└── README.md                 # Project documentation
```

### Key Directories and Files

- **`platformio.ini`**: Configuration file for PlatformIO, specifying the ESP32-S3 board and required libraries.
- **`scripts/`**: Contains Python scripts for firmware dumping, trimming, and revalidating:
  - `dump_and_trim.py`: Dumps firmware from the ESP32 device, extracts the validation hash, and trims the firmware file.
  - `hash.py`: Recalculates and patches the checksum and SHA256 hash for the firmware.
- **`src/main.cpp`**: A dummy program for testing and analysis, using the Adafruit NeoPixel library to control an LED.
- **`decomp/`**: Decompiled firmware files for analysis.

## Requirements

- Python 3.x
- [PlatformIO](https://platformio.org/)
- ESP32-S3 development board
- `esptool.py` for interacting with the ESP32 firmware

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/esp32-firmware-hacking.git
   cd esp32-firmware-hacking
   ```

2. Install PlatformIO:
   ```sh
   pip install platformio
   ```

3. Install required Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Install PlatformIO libraries:
   ```sh
   platformio lib install
   ```

## Usage

### Dumping and Trimming Firmware

1. Connect your ESP32-S3 device to your computer.
2. Run the `dump_and_trim.py` script to dump the firmware and trim it after the validation hash:
   ```sh
   python scripts/dump_and_trim.py
   ```

### Revalidating Firmware

1. Use the `hash.py` script to recalculate and patch the checksum and SHA256 hash:
   ```sh
   python scripts/hash.py
   ```

### Building and Uploading the Dummy Program

1. Build the dummy program using PlatformIO:
   ```sh
   platformio run
   ```

2. Upload the program to the ESP32-S3 device:
   ```sh
   platformio run --target upload
   ```

## Scripts Overview

### `dump_and_trim.py`

- **Purpose**: Dumps firmware from the ESP32 device, extracts the validation hash, and trims the firmware file.
- **Key Functions**:
  - `dump_firmware_from_device(output_path)`: Dumps firmware using `esptool.py`.
  - `get_hash_from_image_info(bin_file)`: Extracts the validation hash from the firmware.
  - `trim_file_after_hash(input_path, output_path, hash_value)`: Trims the firmware file after the validation hash.

### `hash.py`

- **Purpose**: Recalculates and patches the checksum and SHA256 hash for the firmware.
- **Key Functions**:
  - `get_calculated_checksum(bin_file)`: Extracts the calculated checksum from the firmware.
  - `patch_checksum_and_hash(in_path, out_path, checksum)`: Patches the checksum and appends the SHA256 hash.

## Dummy Program

The dummy program in `src/main.cpp` is a simple example that uses the Adafruit NeoPixel library to control an LED. It is intended for testing and analysis purposes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This project is for educational and research purposes only. Use it responsibly and ensure compliance with applicable laws and regulations.