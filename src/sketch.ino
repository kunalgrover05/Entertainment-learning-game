int avg_sensorValue_1=0;
int avg_sensorValue_2=0;
void setup()
{
Serial.begin(115200);    
}

void loop()
{
    int sensorValue_1=analogRead(A5); 
    int sensorValue_2=analogRead(A0);

   if (sensorValue_1==1023 && sensorValue_2<1023) {
	    Serial.println("Correct");
	 } else if (sensorValue_1<1023 && sensorValue_2==1023) { 
	    Serial.println("Wrong");
	 } else if (sensorValue_1<1023 && sensorValue_2<1023) {
	    //Serial.println("You touched both options.");
	 }
	 else{
	 //Serial.println("Touch one of the two.");
	 }
	 delay(1000);

}
