import RPI.GPIO as GPIO
import time
import spidev
from lib_nrf24 import NRF24
import cv2
import time
import numpy as np

class Passenger(object):
  def __init__(self, Power="ON", Battery_level=100, Status="On Board", Priority="Normal", isRider=False, Selected=False):
    self.Power = Power
    self.Battery_level = Battery_level
    self.Status = Status
    self.Priority = Priority
    self.isRider = isRider
    self.Selected = Selected

### GLOBAL VARIABLES
selected

"Pins assigned to buttons coming from physical pannel"
SNSR_Toggle = 3 #pin assigned is GPIO 03
SNSR_Select = 4 #pin assigned is GPIO 04
SNSR_Priority = 5 #pin assigned is GPIO 05
ALRM_Disregard = 6 #pin assigned is GPIO 06

"Pins assigned for NRF communication with Arduino"
CE = 25 #pin assigned is GPIO 25
CSN = 8 #pin assigned is GPIO 08
CK = 11 #pin assigned is GPIO 25
MISO = 9 #pin assigned is GPIO 25
MOSI = 10 #pin assigned is GPIO 25

### RADIO GLOBALS
GPIO.setmode(GPIO.BCM)
passenger_pipe1 = [0xE6, 0xE6, 0xE6, 0xE6, 0xE6] #reading pipe address for communication with Passnger 1
passenger_pipe2 = [0xE7, 0xE7, 0xE7, 0xE7, 0xE7] #reading pipe address for communication with Passnger 2
passenger_pipe3 = [0xE8, 0xE8, 0xE8, 0xE8, 0xE8] #reading pipe address for communication with Passnger 3
passenger_pipe4 = [0xE9, 0xE9, 0xE9, 0xE9, 0xE9] #reading pipe address for communication with Passnger 4
rider_pipe = [0xEA, 0xEA, 0xEA, 0xEA, 0xEA] #reading pipe address for communication with Rider

### FUNCTIONS
def Arduino_Init():
	radio.begin(0,25) #start radio and set CE = GPIO08, CSN = GPIO25
  radio.setPayloadSize(32) #set payload size as 32 bytes
  radio.setChannel(0x76)
  radio.setDataRate(NRF24.BR_1MBPS) #Set radio data rate
  radio.setPALevel(NRF24.PA_MIN) #Set PA level
  radio.setAutoAck(True)
  
def select_passenger(tmp):
  for i in range(len(tmp)):
    if i == len(tmp)-1:
      tmp[i].Selected = False
      tmp[0].Selected = True
      break
    if tmp[i].Selected:
      tmp[i+1].Selected = True
      tmp[i].Selected = False

def toggle_passenger(tmp):
  for psg in tmp:
    if psg.Selected:
      psg.Power = "Off"
      break

def priority_set(tmp):
  for psg in tmp:
    if psg.Selected:
      psg.Priority = "High"
      break
  
def camera_tracking():


### DRIVER CODE
if __name__ == "main":
	# Initializations
  Arduino_Init()
  passengers_list = []
  
  n_passengers = input("Number of passengers on boat")
  rider = input("Will the rider sensor be used? Yes/No")
  for i in range(n):
    passenger = Passenger()
    if i == n-1: passenger.isRider = True
    passengers_list.append(passenger)
  
  if len(passengers_list) != 0: passengers_list[0].Selected = True
  
  #listen for input button press
  if GPIO.input(SNSR_Select): select_passenger(passengers_list)
  if GPIO.input(SNSR_Toggle): toggle_passenger(passengers_list)
  if GPIO.input(SNSR_Priority): priority_set(passengers_list)
  if GPIO.input(ALRM_Disregard): disregard_alarm()



  # Ask user for settings
  # e.g. passenger sensor priority (for babies, dogs, etc.)
  #     turn on propellor, passenger, hand, camera sensor
  #     adjust risk level for each sensor
  # Off state for RPI would not be handled by code...
  # ...physical power should be disconnected (we have one power button)
  
  # Continuous main loop
  previous = time.time()
  while True:
    if time.time() - previous >= 0.5:
      previous = time.time()
      fall = camera_tracking() # Run camera tracking code to check for rider fall

    #listen for input button press
    if GPIO.input(SNSR_Select): select_passenger(passengers_list)
    if GPIO.input(SNSR_Toggle): toggle_passenger(passengers_list)
    if GPIO.input(SNSR_Priority): priority_set(passengers_list)
    if GPIO.input(ALRM_Disregard): disregard_alarm()

    

    


    ### Risk Assessment and Alert Logic (continuous)
