#include <Servo.h>
#include <cvzone.h>
Servo gServo1;
Servo gServo2;
#define sensor1 8
#define sensor2 9
SerialData serialData(2,1);

int valsRec[0];



void setup() {
  // put your setup code here, to run once:
    serialData.begin(9600);
   // pinMode(2,OUTPUT);
    //pinMode(3,OUTPUT);
    //pinMode(4,OUTPUT);
    gServo1.attach(5);
    gServo2.attach(6);
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valsRec);
  /*
  if(valsRec[0] == 0 ){
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
  }
  */
  Serial.println(digitalRead(sensor1));
  if(valsRec[0] == 1 && digitalRead(sensor1)== 0){
    Serial.println(digitalRead(sensor1));
    //digitalWrite(2,HIGH);
    gServo1.write(0);
    delay(1000);
    gServo1.write(120);
    //delay(1000);
    delay(3000);
    
  }
  if(valsRec[0] == 2 && digitalRead(sensor2)== 0){
    Serial.println(digitalRead(sensor2));
    //digitalWrite(3,HIGH);
    gServo2.write(0);
    delay(1000);
    gServo2.write(120);
    //delay(1000);
    delay(3000);
   
  }
}
