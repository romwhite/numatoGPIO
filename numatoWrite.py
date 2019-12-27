import sys
import serial

'''
Use command 'set' to change GPIO pin to HIGH
Use command 'clear' to change GPIO pin to LOW
'''

ser = serial.Serial('COM9', baudrate=19200)
command = "set"
gpioNum = "0"
print("gpio " + command + " " + str(gpioNum))
ser.write(str("gpio " + command + " " + str(gpioNum) + "\r").encode())
ser.close()

