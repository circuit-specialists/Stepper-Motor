/*
   An example sketch for stepper motors, using CW drivers

   written by Jake@circuitspecialists.com
   licensed as GPLv3
*/

const int stepsPerRevolution = 200; // Normal step is 200, Microstep is 1600
const int stepperSpeed = 300; // 300 RPM is fluid
const int CP_plus = 9;
const int CW_plus = 8;

void setup() {
  pinMode(CP_plus, OUTPUT);
  pinMode(CW_plus, OUTPUT);
  digitalWrite(CW_plus, HIGH);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  rotate(270); // rotate motor 270 degrees
  rotate(180, "cw"); // rotate motor 180 degrees clockwise
  rotate(90, "ccw"); // rotate motor 90 degrees counter clockwise
  revolve(5);
  changeDirection("cw");
  revolve(3);
  changeDirection("ccw");
  revolve(8);
}

void rotate(int degrees) {
  steps(degrees / 1.8);
}

void rotate(int degrees, String direction) {
  changeDirection(direction);
  steps(degrees / 1.8);
}

void steps(int amount) {
  double delayTime = 150000.00 / double(stepperSpeed);
  for (int i = 0; i < amount; i++) {
    digitalWrite(CP_plus, HIGH);
    delayMicroseconds(20);
    delayMicroseconds(delayTime);
    digitalWrite(CP_plus, LOW);
    delayMicroseconds(20);
    delayMicroseconds(delayTime);
  }
}

void revolve(int amount) {
  int times = amount * 360;
  steps(times / 1.8);
}

void changeDirection(String direction) {
  if (direction == "cw") {
    digitalWrite(CW_plus, HIGH);
  } else if (direction == "ccw") {
    digitalWrite(CW_plus, LOW);
  }
}
