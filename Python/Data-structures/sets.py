#collection of unique data
#no duplication
#no particular order
#mutable
#unordered, hence no indexing

#create a set
studentID = {12, 14, 16, 18, 20}
print(type(studentID))

#studentID = {12, 12, 14, 16, [8, 20]}#can contain any no of item of diff types but not mutable items eg lists etc
#print(type(studentID))

#empty set
car_values = set()
print(type(car_values))

#duplicate items
launchCodes = {12, 13, 12, 18, 90, 90}
print(launchCodes)

#add items
goals = {20, 4, 8, 90, 71}
goals.add(58)#set.add() takes exactly one argument

print(goals)

#update items
#updates with other collection types eg lists
jezi_no = {11, 16, 21, 10, 7, 9, 49}
midfielders = [5, 6, '4', 3]

jezi_no.update(midfielders)
print(jezi_no)

#remove item
#use discard()

tvModels = {"samsung", "ctc", "tlc", "LG", 67}
#remove 67
remove = tvModels.discard(67)
print(tvModels)

#enumerate
enu = enumerate(tvModels)
print(enu)