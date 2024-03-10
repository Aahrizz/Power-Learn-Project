/*
nameless functions
Lambda or closure

syntax 

    (parameter) {
        //body of anonymous function
    }

    You can assign an anonymous function to a variable
   You can pass an anonymous function as a parameter / argument

 */

 void main() {
  const fruits = ["Apple", "Mango", "Banana", "Orange"];
  List bikes = ["Bmw", "Apache", "Kawasaki", "Yamaha"];

  fruits.forEach((fruit) {
    print(fruit);
  });

  bikes.forEach((bikes) {
   print(bikes);
  }); 
}