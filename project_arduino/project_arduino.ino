#include <dht.h>
dht DHT;
#define DHT11_PIN A0

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  float chk = DHT.read11(DHT11_PIN);
  float sensorsoil = analogRead(A1);
  float soildata = float(map(sensorsoil,1023,45,0,100));
  Serial.print(DHT.humidity);
  Serial.print("/t");
  Serial.print(DHT.temperature);
  Serial.print("/t");
  Serial.print(soildata);
  Serial.println();
  delay(3000);
}
