set1 = set()
set2 = set()

n = int(input("Enter count of numbers: "))

for i in range(n):
    n1 = int(input(f"Enter a set of numbers {i + 1}: "))
    n2 = int(input(f"Enter second set of numbers {i + 1}: "))

    #use add method to add integers to empty set
    set1.add(n1)
    set2.add(n2)

print(set1)
print(set2)

#use intersection to get common number among the sets
common = set1.intersection(set2)
print(f"This set contains coomon elements in both sets {common}")

#set2.update(n2)