# Xbox-EEPROM-Manager
A CircuitPython based original Xbox EEPROM manager, this tool can read, write, and confirm an Xbox's EEPROM.

## Requirements
- A CircuitPython compatible microcontroller (Raspberry Pi Pico, some Arduino boards, etc.)
- A REPL console (Mu, Thonny, etc.)
- Some version of the Original Xbox (I can't confirm that all models work, but I've tested on a 1.0 model)
- This may require a little soldering if your Xbox's debug port doesn't have breakout pins
- You must be willing to break your Xbox warranty seal and connect wires to the motherboard (It's a 20 year old console so it won't change much in terms of warranty)

## Compatibility
This code might not work on all CircuitPython compatible boards, I'll list compatibility here:
Board                      | Compatible | Tested
-------------------------- | --- | ---- |
Feather RP2040             | Yes        | Yes
Raspberry Pi Pico          | Yes        | No
Circuit Playground Express | Yes        | No
Seeduino XIAO              | Yes        | No
QT Py RP2040               | Yes        | No
QT Py (SAMD21)             | Yes        | No
Trinket M0                 | Yes        | No
Arduino Nano RP2040 Connect| Maybe      | No
NeoKey Trinkey - SAMD21    | No         | No
Adafruit Trinkey QT2040    | Yes        | No
Adafruit Feather M4 Express| Yes        | No

You can also tell if a board is compatible if it has an I2C interface and is able to run CircuitPython
# Usage
[Install CircuitPython](https://circuitpython.org/downloads) to your microcontroller if you haven't already\
\
Download and extract ``code.py`` to your CircuitPython's root directory\
\
Change the pin variables to match your board if necessary\
(The default pins are mapped to the [Adafruit Feather RP2040](https://www.adafruit.com/product/4884))\
\
Solder or connect wires to the SCL, SDA, and GND pins on your Xbox motherboard using the below guide:\
![alt text](https://github.com/guighub/Xbox-EEPROM-Manager/blob/main/docs/Xbox-Debug-Pinout.png)

Once soldered, connect them to the according pins you assigned earlier

## Dumping EEPROM:
To dump your EEPROM, simply power up your Xbox followed by powering your microcontroller, you may need to connect the microcontroller to an external power source if you recieve a REPL error about USB connection\
\
You should then recieve a file called ``eeprom.bin`` on the root of the microcontroller, this is your EEPROM dump. You can edit your EEPROM dump using [this tool](https://github.com/Ernegien/XboxEepromEditor)

## Writing EEPROM:
Writing EEPROM is fairly simple. First, save the EEPROM file you would like to write to the root of the microcontroller under the name ``eeprom_edit.bin``\
Now turn on your Xbox followed by your microcontroller, you might see it read the EEPROM first to ``eeprom.bin``, then it should write the ``eeprom_edit.bin`` file to the Xbox's internal EEPROM.

## Confirm EEPROM:
Any time you read or write to your Xbox's EEPROM, the microcontroller will lastly confirm that the EEPROM worked correctly. To check if it read wrong, compare the ``eeprom.bin`` (if reading) or ``eeprom_edit.bin`` (if writing) file to the ``eeprom_result.bin`` file. They should match.

# Issues
I haven't discovered any issues with the current code, but there might be issues with the current error messages not working properly.\
If you have any issues using this program, open an Issue on this repository.
