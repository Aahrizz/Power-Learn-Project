#Create an empty list called my_list.
my_list = list()

#Append the following elements to my_list: 10, 20, 30, 40.
newList = (10, 20, 30, 40)

for i in newList:
    my_list.append(i)

print(my_list)

#Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print(my_list)

#Extend my_list with another list: [50, 60, 70].
list1 = [50, 60, 70]
my_list.extend(list1)

print(my_list)

#Remove the last element from my_list.
del my_list[-1]
print(my_list)

#Sort my_list in ascending order.
my_list.sort()
print(f"Sorted list (ascending): {my_list}")

#Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)

print(f"The index of 30 in the list is: {index_of_30}")