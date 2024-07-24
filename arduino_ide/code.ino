#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <Arduino_JSON.h>

const char* ssid = "WIFI_SSID";
const char* password = "WIFI_PASSWORD";
const String buzzer = "1";
const String ip_address = "192.168.x.x";
const String server_url = "http://" + ip_address + ":5000/b" + buzzer;

unsigned long lastTime = 0;
const int BUTTON_PIN = D7;
const int LED_PIN = D2;


unsigned long timerDelay = 1500;
String jsonBuffer;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("Timer set to 10 seconds (timerDelay variable), it will take 10 seconds before publishing the first reading.");
}

void loop() {
  int button_state = digitalRead(BUTTON_PIN);
  if(button_state == LOW){
    if ((millis() - lastTime) > timerDelay) {
      // Check WiFi connection status
      if(WiFi.status()== WL_CONNECTED){
        String serverPath = server_url;
        jsonBuffer = httpGETRequest(serverPath.c_str());
        Serial.println(jsonBuffer);
        // JSONVar myObject = JSON.parse(jsonBuffer);
        if (jsonBuffer.compareTo("1")){
            Serial.println("LED OFF");
            digitalWrite(LED_PIN, LOW);
        }
        else{
            digitalWrite(LED_PIN, HIGH);
            Serial.println("LED ON");
            delay(1500);
            digitalWrite(LED_PIN, LOW);
        }
      }
      else {
        Serial.println("WiFi Disconnected");
      }
      lastTime = millis();
    }
  }
}

String httpGETRequest(const char* serverName) {
  WiFiClient client;
  HTTPClient http;
    
  // Your IP address with path or Domain name with URL path 
  http.begin(client, serverName);
  
  // Send HTTP POST request
  int httpResponseCode = http.GET();
  
  String payload = "{}"; 
  
  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}