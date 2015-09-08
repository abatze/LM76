#!/usr/bin/python
from I2C import Device 
lm_adress = 0x00
i2c = Device(0x48, 1)
temp = i2c.readS16BE(lm_adress)
ergebnis = temp >> 3
ausgabe = ergebnis * 0.0625

print(ausgabe)

 
