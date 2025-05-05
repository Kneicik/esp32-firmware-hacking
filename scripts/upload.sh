#!/bin/bash

esptool.py --chip esp32s3 --port /dev/cu.wchusbserial595B0150521 \
    write_flash 0x0000 ../.pio/build/esp32s3/bootloader.bin \
    0x8000 ../.pio/build/esp32s3/partitions.bin \
    0x10000 ../firmware_fixed.bin