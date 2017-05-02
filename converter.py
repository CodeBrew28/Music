import requests
import sys 

r = requests.get('http://127.0.0.1:5000/' + sys.argv[1])

color_string = r.content


import serial
ser = serial.Serial('/dev/cu.usbmodem1411', 115200)
print(ser.name)      # check which port was really used
ser.write(str(color_string) )     # write a string
ser.close()             # close port

print(color_string)
