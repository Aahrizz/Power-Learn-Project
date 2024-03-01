#list
ages = [23, 24, 25, 26, 27]

print(ages[0])
print(len(ages))
print(ages)

#list methods
#insert
ages.insert(5, 90)
ages.insert(0, [30, 90])
print(ages)

#append
ages.append([80, 90, 100, "cherry", "python", True, 90.3, 100.78, 90.567])
what = type(ages)
print (what)
print(ages)

#extend
subjects = ["oop", "funcional programming", "format specifiers"]
fundamentals = {"Blockchain", "cryptography", "Data structures"}
subjects.extend(fundamentals)
print(subjects)
#print(type(fundamentals))

#remove
##uses str
presidents = ["Jomo", "Moi", "Kibaki", "UK", "Ruto"]
presidents.remove("Ruto")
print(presidents)

#pop
##uses index to remove
softDrinks = ["cocacola", "fanta", "sprite", "krest", "clubsoda"]
softDrinks.pop(0)
print(softDrinks)

#clear
big5 = ["lion", "leopard", "cheetah", "elephants", "rhino"]
big5.clear()
print(big5)

#index
counties = ["nairobi", "Nyeri", "Nyandarua", "Siaya"]
position = counties.index("Siaya")
print(position)

#count
##outputs occurence of an item in a list
myList = [1, 90.89, 0.99, "Bitcoin", "inflation", False, {"new", "hard"}]
print(myList.count("Bitcoin"))

#sort
junk = ["fries", "soya", "sossi", "23"]
junk.sort()
print(junk)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=False)
print(cars)  # Output: ['Volvo', 'Ford', 'BMW']


#reverse
levels = [1, 2, 3, 5, 6, 7]
print(levels)

#copy
team = ["manu", "manc", "ars"]
##team1 = ["liv", 3, 7, 9]

team1 = team.copy()
print(team1)
print(id(team))
print(id(team1))

#del keyword
languages = ["c", "c++", "haskell", "rust", "ruby", "typescript"]
#del languages[-1]
del languages[0 : 4]
print(languages)


#iterating through a list
ogMovies = ["Godfather", "American psycho", "Scarface", "Avatar", True]
#for loop
for i in ogMovies:
    print(i)


#python list comprehension
#concise and elegant way to create lists.
# consists of an expression followed by the for statement inside square brackets.

names = [number*number for number in range(1, 10)]

print(names)