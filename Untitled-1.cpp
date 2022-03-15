#include <Wire.h>
#include <SD.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)
// your pins
const int chipSelect = 10;

Adafruit_BME280 bme;
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

int PKG = 0;

unsigned long time1 = 0;
unsigned long time2 = 0;

bool isReady = false;

File dataFile;

void printData(imu::Vector<3> vec)
{
  if (isReady && dataFile)
  {
    dataFile.print(vec.x());
    dataFile.print(",");
    dataFile.print(vec.y());
    dataFile.print(",");
    dataFile.print(vec.z());
    dataFile.print(",");
  }
}

void setup()
{
  Serial.begin(9600);
  bme.begin(&Wire);
  bno.begin();
  SD.begin(chipSelect);
  bno.setExtCrystalUse(true);
}

void loop()
{
  isReady = time1 - time2 >= 990;
  time2 = time1;
  dataFile = SD.open("datalog.txt", FILE_WRITE);
  if (isReady)
  {
    dataFile.print(PKG++);
    dataFile.print(",");
    dataFile.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
    dataFile.print(",");
  }

  time1 = millis();

  printData(bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE));

  printData(bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER));

  // printData(bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL));

  // printData(bno.getVector(Adafruit_BNO055::VECTOR_GRAVITY));

  dataFile.println();

  dataFile.close();
}
