#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include "DHT.h"

#define DHTPIN 5 
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

// REST API Endpoint
String RESTAPI  = "http://192.168.0.126:5000/api/v1/sensor/post";
String DEVICE_NAME = "Sensor Node 001";
String DEVICE_NO = "01500000A";

#define SSID_ "AP_IOT"
#define PASSWORD_ "yunusggg"

String Json_Data = "";

void setup()
{
  Serial.begin(9600);
  Serial.print("Connecting to ");
  Serial.println(SSID_);

  WiFi.begin(SSID_, PASSWORD_);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Print the IP address
  Serial.println(WiFi.localIP());

  dht.begin();
}


void sendDatatoRESTAPI(String device_name, String device_no, float temperature, float humidity)
{
    WiFiClient client;
    HTTPClient http;
    http.begin(client, RESTAPI);
    http.addHeader("Content-Type", "application/json");
    Json_Data = "{  \"name\":\"" + device_name + "\"" +
                 ", \"device_no\": \"" + device_no + "\"" +
                 ", \"temperature\": " + String(temperature, 6) + 
                 ", \"humidity\": " + String(humidity, 6) +
                 "}";
    Serial.print (Json_Data);
    int httpCode = http.POST(Json_Data);
      
    // httpCode will be negative on error
    if (httpCode > 0) {
    // HTTP header has been send and Server response header has been handled
      Serial.printf("[HTTP] POST... code: %d\n", httpCode);

      // file found at server
      if (httpCode == HTTP_CODE_OK) {
        const String& payload = http.getString();
        Serial.println("received payload:\n<<");
        Serial.println(payload);
        Serial.println(">>");
      }
    } else {
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  
}


void loop()
{
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);

  sendDatatoRESTAPI(DEVICE_NAME, DEVICE_NO, t, h);
  delay(3000);
}
