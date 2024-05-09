void setup() {
  pinMode(9, OUTPUT); // Set pin 9 as output
  pinMode(10, OUTPUT); // Set pin 10 as output
  pinMode(11, OUTPUT); // Set pin 11 as output
}

void loop() {
  digitalWrite(9, HIGH); // Turn on the green LED
  delay(1000);
  
  digitalWrite(9, LOW);
  digitalWrite(10, HIGH); // Turn on the blue LED
  delay(1000);
  
  digitalWrite(10, LOW);
  digitalWrite(11, HIGH); // Turn on the red LED
  delay(1000);

  digitalWrite(11, LOW);
}