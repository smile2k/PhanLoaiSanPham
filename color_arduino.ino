#include <Servo.h>
#include <cvzone.h>
Servo gServo1;
Servo gServo2;
#define sensor1 8
#define sensor2 9
SerialData serialData(2,1);

int valsRec[0];
int x;
int pos = 0;
String data;

void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    Serial.setTimeout(1);
    serialData.begin(9600);
    // pinMode(2,OUTPUT);
    //pinMode(3,OUTPUT);
    //pinMode(4,OUTPUT);
    gServo1.attach(5);
    gServo2.attach(6);
    
}

void loop() {
  // put your main code here, to run repeatedly:
  //serialData.Get(valsRec);
  //Serial.read(ValsRec[0])
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.println(x);
  //ata= Serial.readString();
  //Serial.println(data);
  /*
  if(valsRec[0] == 0 ){
    digitalWrite(2,LOW);
    digitalWrite(3,LOW);
  }
  */
 
  //1 = RED
  //Serial.println(valsRec[0]);
  while(x == 1 ){
    //Serial.println(digitalRead(sensor1));
    //digitalWrite(2,HIGH);
    //gServo1.write(0);
    
    if(digitalRead(sensor1)== 0){
    delay(2000);
    /*
    for(pos = 90; pos>=1; pos-=1) {                           
        gServo1.write(pos);
        delay(5);
    } 
    for(pos = 0; pos < 90; pos += 1){ 

         gServo1.write(pos);
         delay(5);
    }
    */
      
    gServo1.write(90);
    delay(1000);
    //delay(3000);
    gServo1.write(0);
    delay(1000);
    break;
    }
  }
  // 2 = GREEN
  while(x == 2 ){
    
  //delay(3000);
    if(digitalRead(sensor2)== 0){
      delay(2500);
      /*
      for(pos = 0; pos < 90; pos += 1){ 

         gServo2.write(pos);
         delay(5);
    }
    
      for(pos = 90; pos>=1; pos-=1) {                           
        gServo2.write(pos);
        delay(5);
    } */
    gServo2.write(90);
    delay(1000);
    gServo2.write(0);
    delay(1000);
    break;
    }
  }
}
