class Toyota {
  String model;
  String maker;
  int yom;
  int hp;
  int torque;
  bool power;

  //constructors
  Toyota(
    this.model,
    this.maker,
    this.yom,
    this.hp,
    this.torque,
    this.power
  );

  //method
  String start(){
    String action = "The car has started";
    return action;
  }

  void stop() {
    print("The car has stopped");
  }
}

void main() {
  var myDreamCar = Toyota(
    'Landcruiser 300',
    'Toyota Aussie',
    2016,
    5600,
    5000,
    true
  );

  print("A scoop to features of my dream car");
  myDreamCar.start();
  print("${myDreamCar.model}, ${myDreamCar.maker}, ${myDreamCar.power}");
  myDreamCar.stop();
}