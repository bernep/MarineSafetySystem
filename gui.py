from guizero import *


def select_sensor():
    if pass_1_text.text_color == "red":
        pass_1_text.text_color = pass_3_text.text_color = pass_4_text.text_color = rider_text.text_color = "black"
        pass_2_text.text_color = "red"
    elif pass_2_text.text_color == "red":
        pass_1_text.text_color = pass_2_text.text_color = pass_4_text.text_color = rider_text.text_color = "black"
        pass_3_text.text_color = "red"
    elif pass_3_text.text_color == "red":
        pass_1_text.text_color = pass_2_text.text_color = pass_3_text.text_color = rider_text.text_color = "black"
        pass_4_text.text_color = "red"
    elif pass_4_text.text_color == "red":
        pass_1_text.text_color = pass_2_text.text_color = pass_3_text.text_color = pass_4_text.text_color = "black"
        rider_text.text_color = "red"
    elif rider_text.text_color == "red":
        pass_4_text.text_color = pass_2_text.text_color = pass_3_text.text_color = rider_text.text_color = "black"
        pass_1_text.text_color ="red"
    else: pass_1_text.text_color = "red"

def set_priority():
    if pass_1_text.text_color == "red" and pass_1_power_textbox.value == "ON":
        if pass_1_priority_textbox.value == "Normal":
            pass_1_priority_textbox.value = "High"
            pass_1_priority_textbox.bg = "yellow"
        else:
            pass_1_priority_textbox.value = "Normal"
            pass_1_priority_textbox.bg = "white"
            
    elif pass_2_text.text_color == "red" and pass_2_power_textbox.value == "ON":
        if pass_2_priority_textbox.value == "Normal":
            pass_2_priority_textbox.value = "High"
            pass_2_priority_textbox.bg = "yellow"
        else:
            pass_2_priority_textbox.value = "Normal"
            pass_2_priority_textbox.bg = "white"
    elif pass_3_text.text_color == "red" and pass_3_power_textbox.value == "ON":
        if pass_3_priority_textbox.value == "Normal":
            pass_3_priority_textbox.value = "High"
            pass_3_priority_textbox.bg = "yellow"
        else:
            pass_3_priority_textbox.value = "Normal"
            pass_3_priority_textbox.bg = "white"
        
    elif pass_4_text.text_color == "red" and pass_4_power_textbox.value == "ON":
        if pass_4_priority_textbox.value == "Normal":
            pass_4_priority_textbox.value = "High"
            pass_4_priority_textbox.bg = "yellow"
        else:
            pass_4_priority_textbox.value = "Normal"
            pass_4_priority_textbox.bg = "white"
            
    elif rider_text.text_color == "red" and rider_power_textbox.value == "ON":
        if rider_priority_textbox.value == "Normal":
            rider_priority_textbox.value = "High"
            rider_priority_textbox.bg = "yellow"
        else:
            rider_priority_textbox.value = "Normal"
            rider_priority_textbox.bg = "white"
    
def clear_alert():
    alerts_textbox.clear()
    alerts_text.bg = "white"

def ally_down():
    if pass_1_text.text_color == "red" and pass_1_power_textbox.value == "ON":
        pass_1_on_textbox.value = "Off board"
        pass_1_on_textbox.bg = "red"
        
    elif pass_2_text.text_color == "red" and pass_2_power_textbox.value == "ON":
        pass_2_on_textbox.value = "Off board"
        pass_2_on_textbox.bg = "red"
        
    elif pass_3_text.text_color == "red" and pass_3_power_textbox.value == "ON":
        pass_3_on_textbox.value = "Off board"
        pass_3_on_textbox.bg = "red"
        
    elif pass_4_text.text_color == "red" and pass_4_power_textbox.value == "ON":
        pass_4_on_textbox.value = "Off board"
        pass_4_on_textbox.bg = "red"
        
    elif rider_text.text_color == "red" and Camera_fall.value == 1 and rider_power_textbox.value == "ON":
        rider_on_textbox.value = "Off board"
        rider_on_textbox.bg = "red"
        
    
    testing = []
    testing.append(pass_1_on_textbox.value == "On board")
    testing.append(pass_2_on_textbox.value == "On board")
    testing.append(pass_3_on_textbox.value == "On board")
    testing.append(pass_4_on_textbox.value == "On board")
    testing.append(rider_on_textbox.value == "On board")
    
    if testing.count(False) >= 2:
        alerts_textbox.value = "WARNING: Multiple passengers Off board"
    
    elif pass_1_on_textbox.value == "Off board":
        alerts_text.bg = "red"
        if pass_1_priority_textbox.value == "Normal":
            alerts_textbox.value = "WARNING: Passenger 1 is Off board"
        else:
            alerts_textbox.value = "WARNING: High priority passenger is Off board (Passenger 1)\nMotor is stalled"
            
    elif pass_2_on_textbox.value == "Off board":
        alerts_text.bg = "red"
        if pass_2_priority_textbox.value == "Normal":
            alerts_textbox.value = "WARNING: Passenger 2 is Off board"
        else:
            alerts_textbox.value = "WARNING: High priority passenger is Off board (Passenger 2)\nMotor is stalled"
        
    elif pass_3_on_textbox.value == "Off board":
        alerts_text.bg = "red"
        if pass_3_priority_textbox.value == "Normal":
            alerts_textbox.value = "WARNING: Passenger 3 is Off board"
        else:
            alerts_textbox.value = "WARNING: High priority passenger is Off board (Passenger 3)\nMotor is stalled"
        
    elif pass_4_on_textbox.value == "Off board":
        alerts_text.bg = "red"
        if pass_4_priority_textbox.value == "Normal":
            alerts_textbox.value = "WARNING: Passenger 4 is Off board"
        else:
            alerts_textbox.value = "WARNING: High priority passenger is Off board (Passenger 4)\nMotor is stalled"
        
    elif rider_on_textbox.value == "Off board" and Camera_fall.value == 1:
        alerts_text.bg = "red"
        if rider_priority_textbox.value == "Normal":
            alerts_textbox.value = "WARNING: Rider is Off board"
        else:
            alerts_textbox.value = "WARNING: High priority passenger is Off board (Rider)\nMotor is stalled"
            
def ally_up():
    
    if pass_1_text.text_color == "red" and pass_1_power_textbox.value == "ON":
        pass_1_on_textbox.value = "On board"
        pass_1_on_textbox.bg = "lightgreen"
        
    elif pass_2_text.text_color == "red" and pass_2_power_textbox.value == "ON":
        pass_2_on_textbox.value = "On board"
        pass_2_on_textbox.bg = "lightgreen"
        
    elif pass_3_text.text_color == "red" and pass_3_power_textbox.value == "ON":
        pass_3_on_textbox.value = "On board"
        pass_3_on_textbox.bg = "lightgreen"
        
    elif pass_4_text.text_color == "red" and pass_4_power_textbox.value == "ON":
        pass_4_on_textbox.value = "On board"
        pass_4_on_textbox.bg = "lightgreen"
        
    elif rider_text.text_color == "red" and rider_power_textbox.value == "ON":
        rider_on_textbox.value = "On board"
        rider_on_textbox.bg = "lightgreen"
        
    testing = []
    testing.append(pass_1_on_textbox.value == "On board")
    testing.append(pass_2_on_textbox.value == "On board")
    testing.append(pass_3_on_textbox.value == "On board")
    testing.append(pass_4_on_textbox.value == "On board")
    testing.append(rider_on_textbox.value == "On board")
    
    priorities = []
    priorities.append(pass_1_priority_textbox.value == "High")
    priorities.append(pass_2_priority_textbox.value == "High")
    priorities.append(pass_3_priority_textbox.value == "High")
    priorities.append(pass_4_priority_textbox.value == "High")
    priorities.append(rider_priority_textbox.value == "High")
    
    if testing.count(False) >= 2:
        alerts_textbox.value = "WARNING: Multiple passengers Off board"
    elif testing.count(False) == 0:
        alerts_textbox.clear()
        alerts_text.bg = "white"
        
    else:
        for i in range(5):
            if testing[4] == False:
                if priorities[4] == True: alerts_textbox.value = "WARNING: High priority passenger is Off board (Rider)\nMotor is stalled"
                else: alerts_textbox.value = "WARNING: Rider is Off board"
                break
            if testing[i] == False:
                if priorities[i] == True: alerts_textbox.value = "WARNING: High priority passenger is Off board (Passenger {})\nMotor is stalled".format(i+1)
                else: alerts_textbox.value = "WARNING: Passenger {} is Off board".format(i+1)
    
def set_battery():
    if pass_1_text.text_color == "red" and pass_1_power_textbox.value == "ON":
        pass_1_batt_textbox.value = "{}%".format(Battery_level.value)
        if Battery_level.value <= 20:
            pass_1_batt_textbox.bg = (255, 102, 102)
        
    elif pass_2_text.text_color == "red" and pass_2_power_textbox.value == "ON":
        pass_2_batt_textbox.value = "{}%".format(Battery_level.value)
        if Battery_level.value <= 20:
            pass_2_batt_textbox.bg = (255, 102, 102)
        
    elif pass_3_text.text_color == "red" and pass_3_power_textbox.value == "ON":
        pass_3_batt_textbox.value = "{}%".format(Battery_level.value)
        if Battery_level.value <= 20:
            pass_3_batt_textbox.bg = (255, 102, 102)
        
    elif pass_4_text.text_color == "red" and pass_4_power_textbox.value == "ON":
        pass_4_batt_textbox.value = "{}%".format(Battery_level.value)
        if Battery_level.value <= 20:
            pass_4_batt_textbox.bg = (255, 102, 102)
        
    elif rider_text.text_color == "red" and rider_power_textbox.value == "ON":
        rider_batt_textbox.value = "{}%".format(Battery_level.value)
        if Battery_level.value <= 20:
            rider_batt_textbox.bg = (255, 102, 102)
    
def toggle_sensor():
    if pass_1_text.text_color == "red":
        if pass_1_power_textbox.value == "ON": pass_1_power_textbox.value = "OFF"
        else: pass_1_power_textbox.value = "ON"
        
    elif pass_2_text.text_color == "red":
        if pass_2_power_textbox.value == "ON": pass_2_power_textbox.value = "OFF"
        else: pass_2_power_textbox.value = "ON"
        
    elif pass_3_text.text_color == "red":
        if pass_3_power_textbox.value == "ON": pass_3_power_textbox.value = "OFF"
        else: pass_3_power_textbox.value = "ON"
        
    elif pass_4_text.text_color == "red":
        if pass_4_power_textbox.value == "ON": pass_4_power_textbox.value = "OFF"
        else: pass_4_power_textbox.value = "ON"
        
    elif rider_text.text_color == "red" and Camera_fall.value == 1:
        if rider_power_textbox.value == "ON": rider_power_textbox.value = "OFF"
        else: rider_power_textbox.value = "ON"
    

panel = App(width=1500, height=1000, bg=(204,224,255),title="Alert Panel")


##################################################################################
###################   ALERT PANEL AND MESSAGE TEXTBOX   ##########################
##################################################################################

Alerts = Box(panel, align="top", border=True, width="fill")
Alerts.bg = "white"
alerts_text = Text(Alerts, width="fill", text="Alerts")
alerts_text.text_size = 32
alerts_textbox = TextBox(Alerts, multiline=True, width="fill", height=2, text="Welcome to the Autospot Alert Panel")
alerts_textbox.text_size = 30


###############################################################################
###################   PASSENGER SENSORS STATUS BOX   ##########################
###############################################################################

Sensors = Box(panel, align="top", border=True, width="fill", height=440)
Sensors.bg = (204,224,255)
sensors_text = Text(Sensors, width="fill", text="Sensors")
sensors_text.text_size = 22

#Passenger 1
pass_1 = Box(Sensors, width="fill", border=True, layout="grid", height=80)
pass_1_text = Text(pass_1, text="Passenger 1", grid=[0,0])
pass_1_text.text_size = 17

pass_1_power = Box(pass_1, grid=[0,1])
pass_1_power_text = Text(pass_1_power, text="Power", align="left")
pass_1_power_text.text_size = 14
pass_1_power_textbox = TextBox(pass_1_power, width=10, height=3, align="left", text="ON")
pass_1_power_textbox.text_size = 14
pass_1_power_textbox.bg = "white"

pass_1_batt = Box(pass_1, grid=[1,1])
pass_1_batt_text = Text(pass_1_batt, text="Battery level", align="left")
pass_1_batt_text.text_size = 14
pass_1_batt_textbox = TextBox(pass_1_batt, width=10, height=3, align="left", text="100%")
pass_1_batt_textbox.text_size = 14
pass_1_batt_textbox.bg = "white"


pass_1_on = Box(pass_1, border=True, grid=[2,1])
pass_1_on_text = Text(pass_1_batt, text="Status", align="left")
pass_1_on_text.text_size = 14
pass_1_on_textbox = TextBox(pass_1_batt, width=10, height=3, align="left", text="On board")
pass_1_on_textbox.text_size = 14
pass_1_on_textbox.bg = "lightgreen"

pass_1_priority = Box(pass_1, border=True, grid=[3,1])
pass_1_priority_text = Text(pass_1_batt, text="Priority level", align="left")
pass_1_priority_text.text_size = 14
pass_1_priority_textbox = TextBox(pass_1_batt, width=10, height=3, align="left", text="Normal")
pass_1_priority_textbox.text_size = 14
pass_1_priority_textbox.bg = "white"

#Passenger 2
pass_2 = Box(Sensors, width="fill", border=True, layout="grid", height=80)
pass_2_text = Text(pass_2, text="Passenger 2", grid=[0,0])
pass_2_text.text_size = 17

pass_2_power = Box(pass_2, grid=[0,1])
pass_2_power_text = Text(pass_2_power, text="Power", align="left")
pass_2_power_text.text_size = 14
pass_2_power_textbox = TextBox(pass_2_power, width=10, height=3, align="left", text="ON")
pass_2_power_textbox.text_size = 14
pass_2_power_textbox.bg = "white"

pass_2_batt = Box(pass_2, grid=[1,1])
pass_2_batt_text = Text(pass_2_batt, text="Battery level", align="left")
pass_2_batt_text.text_size = 14
pass_2_batt_textbox = TextBox(pass_2_batt, width=10, height=3, align="left", text="100%")
pass_2_batt_textbox.text_size = 14
pass_2_batt_textbox.bg = "white"

pass_2_on = Box(pass_2, border=True, grid=[2,1])
pass_2_on_text = Text(pass_2_batt, text="Status", align="left")
pass_2_on_text.text_size = 14
pass_2_on_textbox = TextBox(pass_2_batt, width=10, height=3, align="left", text="On board")
pass_2_on_textbox.text_size = 14
pass_2_on_textbox.bg = "lightgreen"

pass_2_priority = Box(pass_2, border=True, grid=[3,1])
pass_2_priority_text = Text(pass_2_batt, text="Priority level", align="left")
pass_2_priority_text.text_size = 14
pass_2_priority_textbox = TextBox(pass_2_batt, width=10, height=3, align="left", text="Normal")
pass_2_priority_textbox.text_size = 14
pass_2_priority_textbox.bg = "white"

#Passenger 3
pass_3 = Box(Sensors, width="fill", border=True, layout="grid", height=80)
pass_3_text = Text(pass_3, text="Passenger 3", grid=[0,0])
pass_3_text.text_size = 17

pass_3_power = Box(pass_3, grid=[0,1])
pass_3_power_text = Text(pass_3_power, text="Power", align="left")
pass_3_power_text.text_size = 14
pass_3_power_textbox = TextBox(pass_3_power, width=10, height=3, align="left", text="ON")
pass_3_power_textbox.text_size = 14
pass_3_power_textbox.bg = "white"

pass_3_batt = Box(pass_3, grid=[1,1])
pass_3_batt_text = Text(pass_3_batt, text="Battery level", align="left")
pass_3_batt_text.text_size = 14
pass_3_batt_textbox = TextBox(pass_3_batt, width=10, height=3, align="left", text="100%")
pass_3_batt_textbox.text_size = 14
pass_3_batt_textbox.bg = "white"

pass_3_on = Box(pass_3, border=True, grid=[2,1])
pass_3_on_text = Text(pass_3_batt, text="Status", align="left")
pass_3_on_text.text_size = 14
pass_3_on_textbox = TextBox(pass_3_batt, width=10, height=3, align="left", text="On board")
pass_3_on_textbox.text_size = 14
pass_3_on_textbox.bg = "lightgreen"
    
pass_3_priority = Box(pass_3, border=True, grid=[3,1])
pass_3_priority_text = Text(pass_3_batt, text="Priority level", align="left")
pass_3_priority_text.text_size = 14
pass_3_priority_textbox = TextBox(pass_3_batt, width=10, height=3, align="left", text="Normal")
pass_3_priority_textbox.text_size = 14
pass_3_priority_textbox.bg = "white"
    
#Passenger 4
pass_4 = Box(Sensors, width="fill", border=True, layout="grid", height=80)
pass_4_text = Text(pass_4, text="Passenger 4", grid=[0,0])
pass_4_text.text_size = 17
    
pass_4_power = Box(pass_4, grid=[0,1])
pass_4_power_text = Text(pass_4_power, text="Power", align="left")
pass_4_power_text.text_size = 14
pass_4_power_textbox = TextBox(pass_4_power, width=10, height=3, align="left", text="ON")
pass_4_power_textbox.text_size = 14
pass_4_power_textbox.bg = "white"
    
pass_4_batt = Box(pass_4, grid=[1,1])
pass_4_batt_text = Text(pass_4_batt, text="Battery level", align="left")
pass_4_batt_text.text_size = 14
pass_4_batt_textbox = TextBox(pass_4_batt, width=10, height=3, align="left", text="100%")
pass_4_batt_textbox.text_size = 14
pass_4_batt_textbox.bg = "white"
    
pass_4_on = Box(pass_4, border=True, grid=[2,1])
pass_4_on_text = Text(pass_4_batt, text="Status", align="left")
pass_4_on_text.text_size = 14
pass_4_on_textbox = TextBox(pass_4_batt, width=10, height=3, align="left", text="On board")
pass_4_on_textbox.text_size = 14
pass_4_on_textbox.bg = "lightgreen"
    
pass_4_priority = Box(pass_4, border=True, grid=[3,1])
pass_4_priority_text = Text(pass_4_batt, text="Priority level", align="left")
pass_4_priority_text.text_size = 14
pass_4_priority_textbox = TextBox(pass_4_batt, width=10, height=3, align="left", text="Normal")
pass_4_priority_textbox.text_size = 14
pass_4_priority_textbox.bg = "white"

#Rider
rider = Box(Sensors, width="fill", border=True, layout="grid", height=80)
rider_text = Text(rider, text="Rider", grid=[0,0])
rider_text.text_size = 17

rider_power = Box(rider, grid=[0,1])
rider_power_text = Text(rider_power, text="Power", align="left")
rider_power_text.text_size = 14
rider_power_textbox = TextBox(rider_power, width=10, height=3, align="left", text="ON")
rider_power_textbox.text_size = 14
rider_power_textbox.bg = "white"
    
rider_batt = Box(rider, grid=[1,1])
rider_batt_text = Text(rider_batt, text="Battery level", align="left")
rider_batt_text.text_size = 14
rider_batt_textbox = TextBox(rider_batt, width=10, height=3, align="left", text="100%")
rider_batt_textbox.text_size = 14
rider_batt_textbox.bg = "white"
    
rider_on = Box(rider, border=True, grid=[2,1])
rider_on_text = Text(rider_batt, text="Status", align="left")
rider_on_text.text_size = 14
rider_on_textbox = TextBox(rider_batt, width=10, height=3, align="left", text="On board")
rider_on_textbox.text_size = 14
rider_on_textbox.bg = "lightgreen"
    
rider_priority = Box(rider, border=True, grid=[3,1])
rider_priority_text = Text(rider_batt, text="Priority level", align="left")
rider_priority_text.text_size = 14
rider_priority_textbox = TextBox(rider_priority, width=10, height=3, align="left", text="Normal")
rider_priority_textbox.text_size = 14
rider_priority_textbox.bg = "white"

##############################################################################
###################   ALERT PANEL BUTTONS   ##################################
##############################################################################

general_buttons = Box(panel, align="top", border=True, width="fill", height=310)

buttons = Box(general_buttons, align="left", border=True, width=400, height=600)
buttons.bg = "white"

buttons_text = Text(buttons, text="Alert Panel buttons")
buttons_text.text_size = 22
Alarm = PushButton(buttons, width=15, height=2, text="DISREGARD ALARM", align="top", command=clear_alert)
Sensor = PushButton(buttons, width=15, height=2, text="SENSOR SELECT", align="top", command=select_sensor)
Toggle = PushButton(buttons, width=15, height=2, text="TOGGLE SENSOR", align="top", command=toggle_sensor)
Priority = PushButton(buttons, width=15, height=2, text="PRIORITY FOR SENSOR", align="top", command=set_priority)

Alarm.bg = (204, 204, 204)
Sensor.bg = (204, 204, 204)
Toggle.bg = (204, 204, 204)
Priority.bg = (204, 204, 204)

##############################################################################################
###################   SIMULATION OF INPUT AND OUTPUTS BOX   ##################################
##############################################################################################

Sim_inputs = Box(general_buttons, align="left", border=True, width="fill", height=700)
Sim_inputs.bg = "yellow"
sim_input_box = Box(Sim_inputs, align="top", border=True, width="fill", height=35)
sim_inputs_text = Text(sim_input_box, text="Simulation I/O parameters")
sim_inputs_text.text_size = 22
input_output_box = Box(Sim_inputs, align="top", border=True, width="fill", height=35)
input_box = Box(input_output_box, align="left", border=True, width="fill", height=35)
output_box = Box(input_output_box, align="right", border=True, width="fill", height=35)
input_text = Text(input_box, text="Inputs")
output_text = Text(output_box, text="Outputs")

#Input buttons box of simulation

left = Box(Sim_inputs, align="left", border=True, width=548, height=460)
left_side_box = Box(left, align="left", width=274, height=460)
left_side_box_2 = Box(left, align="right", width=274, height=460)

Passenger_fall = PushButton(left_side_box, width=15, height=3, text="Passenger fall", command=ally_down)
Passenger_back = PushButton(left_side_box, width=15, height=3, text="Passenger back on", command=ally_up)
Propeller_detection = PushButton(left_side_box, width=15, height=3, text="Propeller detection")
Camera_fall_text = Text(left_side_box_2, width=15, height=2, text="Camera fall detection", size=11)
Camera_fall = Slider(left_side_box_2, start=0, end=1, width=135)
Battery_level_text = Text(left_side_box_2, width=15, height=2, text="Battery level", size=11)
Battery_level = Slider(left_side_box_2, start=0, end=100, width=135)
Battery_level_set = PushButton(left_side_box_2, width=16, height=2, text="Set level", command=set_battery)

#Outpux box of simulation

# right = Picture(Sim_inputs, image="GrassNew.png")

#Setting background colors of differrent button in simulation box

Passenger_fall.bg = "white"
Passenger_back.bg = "white"
Propeller_detection.bg = "white"
Camera_fall_text.bg = "white"
Camera_fall.bg = "white"
Battery_level_text.bg = "white"
Battery_level.bg = "white"
Battery_level_set.bg = "white"


panel.display()