import 'dart:io';
//int sum (x, y) => x * y;

/*void main() {
  int result = sum(10, 9);
  print(result);
}*/

//convert sq kilometres to acres
double converter(sq_km, rate) => sq_km * rate;

void main() {
  var inKm = stdin.readLineSync();
  double inKms = double.parse(inKm);
  var convrRate = 247.1;

  double acres = converter(inKms, convrRate);
  print(acres);
}