#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"


/************************* DHT 22 init *********************************/
#include "DHT.h"

#define DHTPIN 5 
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);


/************************* WiFi Access Point *********************************/

#define WLAN_SSID       "AP_IOT"
#define WLAN_PASS       "yunusggg"

/**************************** MQTT Setup ***********************************/

#define MQTT_SERVER      "broker.hivemq.com"
#define MQTT_PORT         1883
#define TOPIC             "dashboard/sensor002"

String DEVICE_NAME = "Sensor Node 001";
String DEVICE_NO = "01500000A";

String Json_Data = "";

WiFiClient client;

Adafruit_MQTT_Client mqtt(&client, MQTT_SERVER, MQTT_PORT);
//Adafruit_MQTT_Subscribe pan_tilt = Adafruit_MQTT_Subscribe(&mqtt, TOPIC);
Adafruit_MQTT_Publish dht22_sensor = Adafruit_MQTT_Publish(&mqtt, TOPIC);

void setup() {
      
      Serial.begin(115200);
      delay(10);
    
      Serial.println(); Serial.println();
      Serial.print("Connecting to ");
      Serial.println(WLAN_SSID);
    
      WiFi.begin(WLAN_SSID, WLAN_PASS);
      while (WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");
      }
      Serial.println();
    
      Serial.println("WiFi connected");
      Serial.println("IP address: "); Serial.println(WiFi.localIP());

      dht.begin();
      Serial.println();
}

void loop() {
     MQTT_connect();

    float h = dht.readHumidity();
    float t = dht.readTemperature();
    if (isnan(h) || isnan(t)) {
      Serial.println(F("Failed to read from DHT sensor!"));
      return;
    }
    
    Json_Data = "{  \"name\":\"" + DEVICE_NAME + "\"" +
                 ", \"device_no\": \"" + DEVICE_NO + "\"" +
                 ", \"temperature\": " + String(t, 6) + 
                 ", \"humidity\": " + String(h, 6) +
                 "}";


      if (! dht22_sensor.publish(Json_Data.c_str())) {
        Serial.println(F("Failed to Publish data..."));
      } else {
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
      }
      delay(5000); // delay 60 second
}

void MQTT_connect() {
      int8_t ret;
      if (mqtt.connected()) {
            return;
      }
    
      Serial.print("Connecting to MQTT... ");
    
      uint8_t retries = 3;
      while ((ret = mqtt.connect()) != 0) {
           Serial.println(mqtt.connectErrorString(ret));
           Serial.println("Retrying MQTT connection in 5 seconds...");
           mqtt.disconnect();
           delay(5000);
           retries--;
           if (retries == 0) {
                while (1);
           }
      }
      Serial.println("MQTT Connected!");
}
