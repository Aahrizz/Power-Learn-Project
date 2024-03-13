#define an array of 2d

groups = [["Sisters", "Brothers"], ["Father", "Mother"]]

#nested loops
for group in groups:
    for relation in group:
        print(relation) 
        

numbers = [[12, 34], [23, 67], [43, 98]]

for n in numbers:
    print(n)
    for m in n:
        #total = n + m
        print(m) 