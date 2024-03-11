
void main() {
  //initialize variables to store our various data values
  int temp = 90;
  double conversion = 1.8;
  String message = "To conver celcius to farenheit";
  List cities = ["Nairobi CBD", "Nairobi south", "Thika", "Nyahururu", "Kisumu"];
  Map <String, int> temps = {'Nairobi Cbd': 25, 'Nairobi south': 26,
  'Thika': 29, 'Nyahururu': 19
  };

  //RUN SOME RESULTs
  double result = temp * conversion;
  print("$message, $result");

//output each city from the list of cities 
  for (var city in cities) {
    print(city);
}
print("Temperatures of the cities are: $temps");

}