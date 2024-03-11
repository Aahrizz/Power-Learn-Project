//executes block of statement first then checks the condition
void main() {
  var a = 1;
  var last = 5;

  do {
    print("The value is: $a");
    a = a+1; 
  }
    while (a < last);
}