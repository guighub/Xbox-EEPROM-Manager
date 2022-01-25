# Xbox-EEPROM-Manager
A CircuitPython based original Xbox EEPROM manager, this tool can read, write, and confirm an Xbox's EEPROM.

# Usage
[Install CircuitPython](http://circuitpython.org) to your microcontroller if you haven't already\
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
