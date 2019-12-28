import serial

ser = serial.Serial('COM9', baudrate=19200, timeout=1)
command = "read"
gpioNum = "0"
ser.write(str("gpio " + command + " " + str(gpioNum) + "\r").encode())
response = ser.read(25)

#ASCII 1 is 49, ASCII 0 is 48


if(response[-4] == 49):
	print("GPIO " + str(gpioNum) +" is ON")
	
elif(response[-4] == 48):
	print("GPIO " + str(gpioNum) +" is OFF")
else:
    print(response.decode())

	
ser.close()
