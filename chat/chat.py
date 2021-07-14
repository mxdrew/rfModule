#!/usr/bin/env python3

# Import libraries we need
import time
import serial
import threading
import sys

# Sets up the serial port for our RF Modules
ser = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 9600,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS,
  timeout = 1
)

# Creates the global variable needed for later
message = ''


# Function to get and decode the message
def readAndDecode():
    global message
    x = ser.readline()
    while (x.decode() == ''):
        x = ser.readline()
    message = x.decode()

def send(arg1):
    # Transmit your message
    while 1:
        s = sys.stdin.read(1)
        s = s + '\n'
        ser.write(s.encode())
        time.sleep(0.25)

def recieve(arg1):
    global message
    while 1:
        # Get the decoded message and format it
        readAndDecode()
        message = message.replace('\n', '').upper()
        message = readAndDecode()
        print(message)
        time.sleep(0.25)


# Create and start the threads
sendThread = threading.Thread(name='getAndSave', target=send, args=(1,)).start()
recieveThread = threading.Thread(name='action', target=recieve, args=(1,)).start()
