
void main() {
    String message = news();
    print(message);

    int a = 4;
    int b = 9;
    int ans = minus(a, b);
    print("The answer to above function is: $ans");
}
//Function with no parameter and has a return type
String news(){
    return "Shout out to all the hommies fro the east side.";
}

//Function with parameters and a return type
int minus(int a, int b){
    int sub = b - a;
    return sub;
}

