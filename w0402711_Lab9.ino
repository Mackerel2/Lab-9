/////////////////////////////////////
//  EETG 3024 - Advanced Embedded  //
//              Lab 9              //      
// For: Ricardo Bautista-Quintero  //
//     Student: Nick Mac Innis     //
//     Date: February 28, 2021     //
/////////////////////////////////////

#include <Servo.h>        //Precompiled header containing functions for the control of servo motors
Servo RCservo1, RCservo2; //Two objects for controlling servo motors
int i = 0, count1 = 0, count2 = 0;
int motor1[5], motor2[5];
void setup()
{
  Serial.begin(9600);     //Set baudrate of arduino, 9600
  RCservo1.attach(10);    //Servo 1 will be controlled by digital pin 10
  RCservo2.attach(11);    //Servo 2 will be controlled by digital pin 11
  
}

void loop()
{
  
  if(Serial.available()>0)    //If serial is available the following code will run
  {
    if(i == 0)
    {
      int data = Serial.parseInt(); //
      RCservo1.write(data);     //Set the servo motor to the position read via serial connection
      //motor1[count1] = data;
      delay(1000);              //Delay loop for one second
      i++;
      count1++;
    }
    else if(i==1)
    {
      int data2 = Serial.parseInt();
      RCservo2.write(data2);
      delay(1000); 
      //motor2[count2] = data2;
      i--;
      count2++;
    }
  }
}
