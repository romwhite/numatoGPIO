import serial
import threading

ser = serial.Serial('COM9', baudrate=19200, timeout=1)


#ASCII 1 is 49, ASCII 0 is 48


def printData():
    print("Button pressed")

def readPort(ser):
    while True:
        command = "read"
        gpioNum = "0"
        ser.write(str("gpio " + command + " " + str(gpioNum) + "\r").encode())
        response = ser.read(25)
        if(response[-4] == 49):
            printData()

thread = threading.Thread(target=readPort, args=(ser,))
thread.start()
