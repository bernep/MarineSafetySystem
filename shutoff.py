#IED
#Section06
#AutoSpot
#Shut Off System
#This code is used to provide a visual simulation of the trigger levels and
    #the reaction of the motor.

print("When a trigger level is indicated, the following occur: ")
range = [0, 10]
state_running = 0
#power is being sent to the motor
#stop_actions
stop_action_coast = 1
#power removed from motor, coast to a stop
stop_action_brake = 2
#power removed from motor, shorting motor terminals together
stop__action_hold = 60
#hold the motor at the current position
state_stalled = 60
#motor is not turning
state_holding = 60
