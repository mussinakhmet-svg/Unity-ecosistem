#include <Arduino.h>

#define RLED 6
#define GLED 5
#define BLED 3
#define BUTTON 2

bool lastButton = LOW;
bool currentButton = LOW;
int ledMode = 0;

bool debounce(bool last);
void setMode(int mode);

void setup() {
  pinMode(RLED, OUTPUT);
  pinMode(GLED, OUTPUT);
  pinMode(BLED, OUTPUT);
  pinMode(BUTTON, INPUT);
}

bool debounce(bool last) {
  bool current = digitalRead(BUTTON);
  if (last != current) {
    delay(5);
    current = digitalRead(BUTTON);
  }
  return current;
}

void setMode(int mode) {
  if (mode == 1) {
    digitalWrite(RLED, HIGH);
    digitalWrite(GLED, LOW);
    digitalWrite(BLED, LOW);
  } else if (mode == 2) {
    digitalWrite(RLED, LOW);
    digitalWrite(GLED, HIGH);
    digitalWrite(BLED, LOW);
  } else if (mode == 3) {
    digitalWrite(RLED, LOW);
    digitalWrite(GLED, LOW);
    digitalWrite(BLED, HIGH);
  } else if (mode == 4) {
    analogWrite(RLED, 127);
    analogWrite(GLED, 0);
    analogWrite(BLED, 127);
  } else if (mode == 5) {
    analogWrite(RLED, 0);
    analogWrite(GLED, 127);
    analogWrite(BLED, 127);
  } else if (mode == 6) {
    analogWrite(RLED, 127);
    analogWrite(GLED, 127);
    analogWrite(BLED, 0);
  } else if (mode == 7) {
    analogWrite(RLED, 85);
    analogWrite(GLED, 85);
    analogWrite(BLED, 85);
  } else {
    digitalWrite(RLED, LOW);
    digitalWrite(GLED, LOW);
    digitalWrite(BLED, LOW);
  }
}

void loop() {
  currentButton = debounce(lastButton);
  if (lastButton == LOW && currentButton == HIGH) {
    ledMode++;
  }
  lastButton = currentButton;
  if (ledMode == 8) ledMode = 0;
  setMode(ledMode);
}