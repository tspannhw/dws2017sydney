#! /usr/bin/python

import os
from gps import *
from time import *
import time
import threading
import json
import time
import colorsys
import os
import json
import sys, socket
import subprocess
import time
import datetime
from time import sleep
from time import gmtime, strftime
import signal
import time
import urllib2

# Need sudo apt-get install gpsd gpsd-clients python-gps ntp
# Based on
#Author: Callum Pritchard, Joachim Hummel
#Project Name: Flick 3D Gesture
#Project Description: Sending Flick 3D Gesture sensor data to mqtt
#Version Number: 0.1
#Date: 15/6/17
#Release State: Alpha testing
#Changes: Created
# Based on
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

# Based on:  https://hortonworks.com/tutorial/analyze-iot-weather-station-data-via-connected-data-architecture/section/3/

#### Initialization
# yyyy-mm-dd hh:mm:ss
currenttime= strftime("%Y-%m-%d %H:%M:%S",gmtime())

external_IP_and_port = ('198.41.0.4', 53)  # a.root-servers.net
socket_family = socket.AF_INET

host = os.uname()[1]

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def IP_address():
        try:
            s = socket.socket(socket_family, socket.SOCK_DGRAM)
            s.connect(external_IP_and_port)
            answer = s.getsockname()
            s.close()
            return answer[0] if answer else None
        except socket.error:
            return None

# Get Raspberry Pi Serial Number
def get_serial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial

# Get Raspberry Pi Public IP via IPIFY Rest Call
def get_public_ip():
  ip = json.load(urllib2.urlopen('https://api.ipify.org/?format=json'))['ip']
  return ip

cpuTemp=int(float(getCPUtemperature()))
ipaddress = IP_address()
# Attempt to get Public IP
public_ip = get_public_ip()

# Attempt to get Raspberry Pi Serial Number
serial = get_serial()

gpsd = None

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  stopthis = False
  try:
    gpsp.start() # start it up
    while not stopthis:
      if gpsd.fix.latitude > 0:
        row = { 'latitude': str(gpsd.fix.latitude),
         'longitude': str(gpsd.fix.longitude),
         'utc': str(gpsd.utc),
         'time':   str(gpsd.fix.time),
         'altitude': str(gpsd.fix.altitude),
         'eps': str(gpsd.fix.eps),
         'epx': str(gpsd.fix.epx),
         'epv': str(gpsd.fix.epv),
         'ept': str(gpsd.fix.ept),
         'speed': str(gpsd.fix.speed),
         'climb': str(gpsd.fix.climb),
         'track': str(gpsd.fix.track),
         'ts': currenttime,
         'public_ip': public_ip,
         'serialno': serial,
         'host': host,
         'cputemp': round(cpuTemp,2),
         'ipaddress': ipaddress,
         'mode': str(gpsd.fix.mode)}
        json_string = json.dumps(row)
        print json_string
	gpsp.running = False
        stopthis = True

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
