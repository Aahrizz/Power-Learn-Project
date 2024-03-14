class Student {
  //properties
  String name;
  String mail;
  int age;
  int grade;


//constructor

Student(this.name, this.mail, this.age, this.grade);

//methods

void run() {
  print("You should be on running mode for your own good");
}
}

void main() {
  var theStudent = Student('Jeffrey Komo', 'komojay0@gmail.com', 22, 12);

  // Accessing properties
  print('Name: ${theStudent.name}');
  print('Email: ${theStudent.mail}');
  
  theStudent.run();
}