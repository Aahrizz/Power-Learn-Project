import 'dart:io';

void main() {
  //print message to prompt for number
  stdout.write("Enter a number: ");
//prompts user input
  String? num = stdin.readLineSync();

if (num != null) {
  int number = int.parse(num);

  if (number > 10) {
    print("Your number is greater than 10");
  } else if (number < 10) {
    print("Your number is less than 10");
  } else if(number == 10) {
    print("Your number is equal to 10");
  } else {
    print("Invalid input. Please enter a valid number");
  }
}
}