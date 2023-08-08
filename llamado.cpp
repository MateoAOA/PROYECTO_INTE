#include <Arduino.h>

const int trigPin = 5;
const int echoPin = 4;

const int buttonPin = 0;

int distance;
bool buttonState = false;
bool lastButtonState = false;

void setup() {
  Serial.begin(9600);
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  
  if (buttonState != lastButtonState) {
    Serial.println(buttonState == HIGH ? F("Botón activado") : F("Botón desactivado"));
    lastButtonState = buttonState;
  }
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  int duration = pulseIn(echoPin, HIGH);
  float distance = duration * 0.034 / 2.0;

  
  if (distance < 100) {
    Serial.println(F("¡Movimiento detectado!"));
  }
  
  delay(500);  // Reducido el tiempo de retardo

}