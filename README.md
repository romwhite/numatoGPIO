# numatoGPIO
Scripts to control Numato USB GPIO board

I recently purchased an 8 channel USB GPIO board from Numato. Using PuTTY and Rhea I found the board worked as it should, but their sample Python scripts were not working. I made these scripts to work properly with Python3. 

**numatoWrite.py** tests tests the function of turning on/off an LED connected to pin 0.

**numatoRead.py** tests reading a simple button connected to pin 0. 

**numatoReadNonBlocking.py** uses threading to leave the script running and continues to print if the button is pressed multiple times while running. Without this the numatoRead.py script will simply tell you whether the button is pressed at the time it is run only. 
