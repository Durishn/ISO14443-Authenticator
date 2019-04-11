#!/usr/bin/env python2

import serial
import datetime
import time
from subprocess import Popen, PIPE
from config import Config

# Logging  
logfile = open("log.txt","a")

#Set serial input
ser = serial.Serial(port=Config.PORT, baudrate=Config.BAUDRATE, timeout=1)

#Unlock script
scpt = '''
    tell application "System Events"
		if name of every process contains "ScreenSaverEngine" then
			tell application "ScreenSaverEngine"
				quit
			end tell
			delay 0.1
 		else 
		tell application "Terminal"
			do shell script "caffeinate -u -t 1"
			end tell
			delay 0.1
		end if
		tell application "System Events" to tell process "loginwindow"
			activate
			delay 0.1
            tell window "Login Panel"
                keystroke "password"
                keystroke return
            end tell
		end tell
	end tell'''

scpt = scpt.replace("password", Config.MAC_PASS)

#Unlock function
def unlock_mac():
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(scpt)
	#print (p.returncode, stdout, stderr)


#Main Process
print("Starting ISO1443 Validator.\nPlease scan an ISO1443A Tag for validation...\n")
while 1:
	validKey = False
	tagType = ''
	outputStr = ''
	arduinoData = ser.readline()

	if arduinoData != "":
		if len(arduinoData) < 10:
			tagType = 'MiFare Classic ISO1443'
		else:
			tagType = 'MiFare UltraLight ISO1443A'

		for x in Config.VALID_UIDS:
			if x in arduinoData:
				validKey = True
				outputStr = "VALID LOGIN: \n\tTIME - "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"\n\tKEY_TYPE - "+tagType+"\n\tKEY_UID - "+arduinoData[:5]+"*****\n"
				print(outputStr)
				logfile.write(outputStr+"\n")
				unlock_mac()

		if validKey == False:
			outputStr = "INVALID ATTEMPT: \n\tTIME - "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')+"\n\tKEY_TYPE - "+tagType+"\n\tKEY_UID - "+arduinoData
			print(outputStr)
			logfile.write(outputStr+"\n")

logfile.close()