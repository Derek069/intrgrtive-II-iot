import requests
import serial
ser = serial.Serial(port='COM3',baudrate= 115200, timeout=1)
def getSerial():
    scan = ser.readline()
    id = scan.decode("utf-8")
    sentId = str(id[:-1])
    return sentId
        

