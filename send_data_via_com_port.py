import serial
import time

SerialObj = serial.Serial('COM7') # COMxx   format on Windows
                                   # ttyUSBx format on Linux

SerialObj.baudrate = 115200  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

time.sleep(1)

# SerialObj.write(b'G01 X5 F100\r\n')      #transmit 'A' (8bit) to micro/Arduino
SerialObj.write(bytearray('G01 X50 F100\r\n','ascii'))

SerialObj.close()          # Close the port