#include "SPI.h"
#include <LiquidCrystal.h>

struct package // Transmission data
{
  int package_id = 1;
  int passenger_id = 1; // This is set based on the passenger
  float battery_power = 100; // Changes based on available power
  bool is_on = false; // Tells central control that sensor is on/off
  bool rider_check = false;
};

typedef struct package Package;
Package data;

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 10, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// initialize ON/OFF states
int PB = 7; //the pin where we connect the button
int LED = 13; //the pin we connect the LED
int global_state = 0; // Read the state of the button

void setup() // Initialization
{
  pinMode(PB, INPUT); //set the button pin as INPUT
  pinMode(LED, OUTPUT); //set the LED pin as OUTPUT
  
  lcd.begin(16,2);              // columns, rows.  use 16,2 for a 16x2 LCD, etc.
  lcd.clear();                  // start with a blank screen
    
  lcd.setCursor(0,0);           // set cursor to column 0, row 0 (the first row)
  lcd.print("Autospot");
  delay(500);
  lcd.setCursor(0,1);           // set cursor to column 0, row 1
  lcd.print("Initializing...");
  
  lcd.setCursor(15, 1);  
  lcd.write(byte(0));
  
  Serial.begin(115200);
  delay(1000);
  lcd.clear();
}

void loop() // Loop message transmission
{
  // Determine if Transmitter is ON or OFF
  int current_state = digitalRead(PB); // Read the state of the button
  if (current_state == 1) {
     if (global_state == 0) {
        digitalWrite(LED, HIGH); // LED is ON to signify transmitter is on
        global_state = 1;
        data.is_on = true;
     } else {
        digitalWrite(LED, LOW); // LED is OFF to signify transmitter is off
        global_state = 0;
        data.is_on = false;
     }
     delay(1000); // wait 1 second for ensuring ON/OFF state
  }
  
  // Keep LED on to signify the transmitter is working
  if (global_state == 1) digitalWrite(LED, HIGH);
  
  // Read battery analog voltage value
  int sensor_value = analogRead(A2); // Read the A2 pin value
  data.battery_power = sensor_value/10; // Convert the value to digital %
  if (data.battery_power == 102) data.battery_power -= 2; // A/D conversion fix 

  // Transmit Data
  if (data.is_on) {
    lcd.setCursor(7,0);
    lcd.print("  ");
    lcd.setCursor(0,0);
  	lcd.print("Pack: ");
  	lcd.setCursor(6,0);
  	lcd.print(data.package_id);
  	lcd.setCursor(9,0);
  	lcd.print("Pass: ");
  	lcd.setCursor(15,0);
  	lcd.print(data.passenger_id);
  	lcd.setCursor(0,1);
  	lcd.print("Batt:" );
  	lcd.setCursor(6,1);
  	lcd.print(data.battery_power);
  }
  else {
    lcd.clear();
    lcd.print("Transmission OFF");
    data.package_id = 0;
  }

  // Final Stuff
  data.package_id = data.package_id + 1; // Package ID increase
  delay(500); // wait 500ms between each transmission
}