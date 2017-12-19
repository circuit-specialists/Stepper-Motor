/*
   An example sketch for stepper motors, using CW drivers

   written by Jake@circuitspecialists.com
   licensed as GPLv3
*/

int stepsPerSecond = 200;
int CP_plus = 9;
int CW_plus = 8;

void setup() {
  pinMode(CP_plus, OUTPUT);
  pinMode(CW_plus, OUTPUT);
  digitalWrite(CW_plus, HIGH);
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
  double delayTime = (1 - (.0000002 * 2)) / stepsPerSecond / 2;
  for (int i = 0; i < amount; i++) {
    digitalWrite(CP_plus, HIGH);
    delayMicroseconds(delayTime);
    digitalWrite(CP_plus, LOW);
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

