void main() {
  var list = [10,20,30,40,50];
  var magari = ["Toyota", "Mazda", "Bmw", "Nissan", "Tesla"];
  for (var num in list) {
    print(num);
  }

  for (var gari in magari) 
  {
    print("We ship: $gari");
  }
}