#include <SPI.h>
#include <nRF24L01.h>             //Downlaod it here: https://www.electronoobs.com/eng_arduino_NRF24.php
#include <RF24.h>            
/*//////////////////////////////////////////////////////*/

/*Create a unique pipe out. The receiver has to 
  wear the same unique code*/  
const uint64_t pipeIn = 0xE8E8F0F0E1LL; //IMPORTANT: The same as in the receiver!!!
/*//////////////////////////////////////////////////////*/

/*Create the data struct we will send
  The sizeof this struct should not exceed 32 bytes
  This gives us up to 32 8 bits channals */
RF24 radio(9, 10); // select  CSN and CE  pins
struct MyData {
  byte pot_value;  
};
int LED = 3;
MyData data;
/*//////////////////////////////////////////////////////*/

//This function will only set the value to  0 if the connection is lost...
void resetData() 
{
  data.pot_value = 0;  
}

/**************************************************/

void setup()
{  
  pinMode(LED,OUTPUT);
  Serial.begin(9600); //Set the speed to 9600 bauds if you want.
  //You should always have the same speed selected in the serial monitor
  resetData();
  radio.begin();
  radio.setAutoAck(false);
  radio.setDataRate(RF24_250KBPS);  
  radio.openReadingPipe(1,pipeIn);
  //we start the radio comunication
  radio.startListening();
}

/******Reset the received data to 0 if connection is lost******/
unsigned long lastRecvTime = 0;
void recvData()
{
  while ( radio.available() )
  {
    radio.read(&data, sizeof(MyData));
    lastRecvTime = millis(); //here we receive the data
  }
}
/**************************************************************/

void loop()
{
recvData();
unsigned long now = millis();
//Here we check if we've lost signal, if we did we reset the values 
if ( now - lastRecvTime > 1000 ) {
// Signal lost?
resetData();
}

Serial.print("Potentiometer: "); Serial.println(data.pot_value);
if  (data.pot_value <50)
analogWrite(LED,400);
else 
analogWrite(LED,0);
delay(100);
}
