class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def intro(self):
        print("Hello everyone, I am", self.name, self.age, "years old and", self.gender)
        
Perp1 = Person('Evans', 34, 'Male')
Perp1.intro()