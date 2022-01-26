# Code written by guiguig
# https://github.com/guighub
# Thanks to Adafruit's Discord for help!

import board
import busio
import digitalio
import time
import storage

EEPROM_ADDRESS = 0x54
EEPROM_SIZE = 256
FILE_NAME = "eeprom_edit.bin"
RESULT_FILE_NAME = "eeprom_result.bin"
result = bytearray(EEPROM_SIZE)
LED = digitalio.DigitalInOut(board.D13) # Internal LED (board.D13 for RP2040 Feather)
LED.direction = digitalio.Direction.OUTPUT


def LED_On():
    while True:
        LED.value = True


# Define I2C
try:
    i2c = busio.I2C(board.A1, board.A0) # I2C Pins connected to Xbox
except:
    print("Xbox connection not found!")
    LED_On()

# Set lock on EEPROM
while not i2c.try_lock():
    pass

# Open EEPROM file on internal memory
try:
    with open(FILE_NAME, "rb") as fp:
        FILE = fp.read(EEPROM_SIZE)
except:
    print("Error reading EEPROM file")
    LED_On()

# Start writing
try:
    print("Writing EEPROM...")
    for i in range(len(FILE)):
        print(chr(FILE[i]), end="")
        # Write one byte at a time
        i2c.writeto(EEPROM_ADDRESS, bytes([i, FILE[i]]))
        time.sleep(0.005)
    print("Done!")
except:
    print("Error writing EEPROM")
    pass

# Confirm results wrote correctly
try:
    print("Confirming EEPROM...")
    read_buffer = bytearray(len(FILE))
    for i in range(len(FILE)):
        # Read one byte at a time
        i2c.writeto_then_readfrom(
            EEPROM_ADDRESS, bytes([i]), read_buffer, in_start=i, in_end=i + 1
        )
    print("Done!")
except:
    print("Error reading EEPROM")
    pass

# Try to save confirmation results (will not work if being used through USB)
try:
    storage.remount("/", False)
    with open(RESULT_FILE_NAME, "wb") as fp:
        fp.write(read_buffer, EEPROM_SIZE)

except:
    print("USB storage active, did not write result file")
    pass

# Finish up
i2c.unlock
