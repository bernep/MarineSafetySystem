#include "RF24.h"
#include "SPI.h"

RF24 radio(9,10); // NRF24L01 used SPI pins + Pin 9 and 10 on the NANO

struct package // Transmission data
{
  int package_id = 1; // Which package of data is being sent
  int passenger_id = 1; // This is set based on the passenger
  float battery_power = 100; // Changes based on available power
  bool is_on = false; // Tells central control that sensor is on/off
  bool rider_check = false; // Tells cental control that this is a passenger
};

typedef struct package Package;
Package data;

// Radio initialization
const uint64_t pipe = 0xE6E6E6E6E6E6; // Receiver should use the same pipe

// Initialize ON/OFF states
int PB = 7; //the pin where we connect the button
int LED = 13; //the pin we connect the LED
int global_state = 0; // Read the state of the button

void setup() // Full initialization
{
  pinMode(PB, INPUT); //set the button pin as INPUT
  pinMode(LED, OUTPUT); //set the LED pin as OUTPUT

  // Radio parameters
  Serial.begin(115200);
  delay(1000);
  radio.begin();
  radio.setChannel(115); 
  radio.setPALevel(RF24_PA_MAX);
  radio.setDataRate(RF24_250KBPS); 
  radio.openWritingPipe(pipe);
  delay(1000);
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
  radio.write(&data, sizeof(data)); 
  Serial.print("\nPackage: ");
  Serial.print(data.package_id);
  Serial.print("\nPassenger: ");
  Serial.print(data.passenger_id);
  Serial.print("\nBattery Power: ");
  Serial.print(data.battery_power);
  Serial.print("\n");
  Serial.print(data.text);
  Serial.print("\n");

  // Final Stuff
  data.package_id = data.package_id + 1;
  delay(500); // Rerun loop every 0.5s
}