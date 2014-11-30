import sys
import pyttsx
import serial
import time

def readOut(str1):
	engine = pyttsx.init()
	rate = engine.getProperty('rate')

	engine.setProperty('rate', rate-60)
	#for voice in voices:
	voice = engine.getProperty('voice')
	engine.setProperty('voice', 2)
	engine.say(str1)
	engine.runAndWait()

def init(k):
	engine = pyttsx.init()
	#voices = engine.getProperty('voices')
	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60)
	#for voice in voices:
	voice = engine.getProperty('voice')
	engine.setProperty('voice', 2)
	engine.say('Hello!')
	engine.say('The question for you is')
	engine.say(k[1])
	engine.say('Option 1 is:')
	engine.say(k[2])
	engine.say('Option 2 is:')
	engine.say(k[3])
	engine.say('Touch the correct option')
	engine.runAndWait()



k=sys.argv;
init(k)
ser=serial.Serial()
ser.baudrate=115200
ser.port='/dev/ttyUSB1'
# '/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_75335313437351410232-if00'''
ser.open()
ser.flushInput()
ser.flushOutput()

while True:
	if ser.inWaiting():
		str1 = ser.readline()
		readOut(str1)
