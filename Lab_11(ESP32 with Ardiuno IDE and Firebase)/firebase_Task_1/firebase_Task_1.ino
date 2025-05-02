#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// WiFi Credentials
const char* ssid = "ME.";
const char* password = "--_--_--_";

// Firebase
const String FIREBASE_HOST = "lab11-1366-default-rtdb.firebaseio.com";
const String FIREBASE_AUTH = "m5Xr4KLCsG8ydCOi5aOIdAQ3oUqCzmxKspJJglbq";
const String FIREBASE_PATH = "/sensor_data.json";

// DHT Sensor
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// OLED Setup
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Timers
const unsigned long SEND_INTERVAL = 10000;
const unsigned long SENSOR_DELAY = 2000;
unsigned long lastSendTime = 0;
unsigned long lastReadTime = 0;

// ======= Setup ======= //
void setup() {
  Serial.begin(115200);
  Wire.begin(8, 9); // I2C default pins (SDA: 21, SCL: 22)
  
  // OLED init
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println("OLED init failed!");
    while (true);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("ESP32-S3 DHT + Firebase");
  display.display();
  delay(1500);

  dht.begin();
  connectWiFi();
}

// ======= Main Loop ======= //
void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    connectWiFi();
  }

  if (millis() - lastReadTime >= SENSOR_DELAY) {
    float temp = dht.readTemperature();
    float hum = dht.readHumidity();

    if (!isnan(temp) && !isnan(hum)) {
      Serial.printf("Read: %.1f°C, %.1f%%\n", temp, hum);
      displaySensorData(temp, hum);

      if (millis() - lastSendTime >= SEND_INTERVAL) {
        sendToFirebase(temp, hum);
        lastSendTime = millis();
      }
    } else {
      Serial.println("DHT read failed");
      displayMessage("Sensor error!");
    }

    lastReadTime = millis();
  }
}

// ======= Functions ======= //
void connectWiFi() {
  displayMessage("Connecting WiFi...");
  Serial.print("Connecting to WiFi");

  WiFi.disconnect(true);
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 15) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWiFi Connected!");
    displayMessage("WiFi Connected!");
  } else {
    Serial.println("\nWiFi Failed!");
    displayMessage("WiFi Failed!");
  }
}

void sendToFirebase(float temp, float hum) {
  if (WiFi.status() != WL_CONNECTED) {
    displayMessage("WiFi lost...");
    return;
  }

  HTTPClient http;
  String url = "https://" + FIREBASE_HOST + FIREBASE_PATH + "?auth=" + FIREBASE_AUTH;
  String jsonPayload = "{\"temperature\":" + String(temp) +
                       ",\"humidity\":" + String(hum) +
                       ",\"timestamp\":" + String(millis() / 1000) + "}";

  Serial.println("Sending to Firebase:");
  Serial.println(jsonPayload);
  displayMessage("Sending to Firebase");

  http.begin(url);
  http.addHeader("Content-Type", "application/json");
  int httpCode = http.POST(jsonPayload);

  if (httpCode == HTTP_CODE_OK) {
    Serial.println("Data sent!");
    displayMessage("Sent to Firebase!");
  } else {
    Serial.printf("Send error: %d\n", httpCode);
    displayMessage("Send Failed!");
  }

  http.end();
}

void displayMessage(String msg) {
  display.clearDisplay();
  display.setCursor(0, 25);
  display.println(msg);
  display.display();
}

void displaySensorData(float temp, float hum) {
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Temp: ");
  display.print(temp);
  display.println(" C");

  display.print("Hum:  ");
  display.print(hum);
  display.println(" %");

  display.setCursor(0, 40);
  display.println("Ready to Send...");
  display.display();
}
