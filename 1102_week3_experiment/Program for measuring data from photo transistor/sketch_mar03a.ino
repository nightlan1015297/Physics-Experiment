void setup() {
  pinMode(A0,INPUT);
  Serial.begin(9600);
}

void loop() {
  int var = analogRead(A0);
  Serial.println(var);
}
