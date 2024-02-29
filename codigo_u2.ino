

int led_1 = 6; // Aqui se selecciona la salida 1
int led_2 = 7; // Aqui se selecciona la salida 2

int valor_voltaje = A2; //Aqui se selecciona la entrada analogica


char dato;
void setup() {
  
  pinMode (led_1,OUTPUT);
  pinMode (led_2,OUTPUT);
  pinMode (valor_voltaje,INPUT);

  Serial.begin(9600);

}

void loop() {
  
    int valor_Serial = analogRead(valor_voltaje);
  float valor_Serial_float = (5.0/1023)*valor_Serial;
  Serial.println(valor_Serial_float);
  delay(500);

  if (Serial.available()>0)
  {
    dato=Serial.read();
    if(dato == '1')
    {
      digitalWrite(led_1,HIGH);
    }
    if(dato == 'A')
    {
      digitalWrite(led_2,HIGH);
    }
    if(dato == '2')
    {
      digitalWrite(led_1,LOW);
    }
    if(dato == 'B')
    {
      digitalWrite(led_2,LOW);
    }
  }


}
