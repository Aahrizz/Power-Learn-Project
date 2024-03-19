//An object-oriented model that uses classes and inheritance

class Student{
  String grade;
  String name;
  var house;
  String admNo;

  Student(
    this.admNo,
    this.grade,
    this.house,
    this.name
  );
}

class bluey extends Student{
    int age;
    int height;
    String remarks;

    bluey(
      this.age, this.height, this.remarks, String grade, String name, var house, String admNo)
      : super(admNo, grade, house, name);
}


void main() {
  var p1 = bluey(15, 176, "Baller", "seven", "Whos", 8, "889");
  var p2 = bluey(16, 179, "Athlete", "eight", "bob", 5, "7764");
  var p3 = bluey(14, 166, "Midget", "Six", "Alice", 6, "9990");

  print("WE request Jeffrey who is ${p1.age}, ${p2.height}cm, and a ${p3.remarks} to report kesho");
}