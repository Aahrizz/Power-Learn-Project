count = float(input("Enter any number between -1 and 1: "))

if (count > 0):
    print(True)
elif (count < 0):
    print(False)


grade = int(input("Enter your finals score: "))
one = ("A, excellent")
two = ("B, good")
three = ("C, average")
four = ("D, bad")
five = ("F, fail")
if(grade >= 70):
    print(f"You scored {grade} which is an {one}")
elif (grade >= 60):
    print(f"You scored {grade} which is a {two}")
elif (grade >= 50):
    print(f"Yyou scored {grade} which is a {three}")
elif (grade >= 40):
    print(f"You scored {grade} which is a {four}")
else:
    print(f"You scored {grade} which is a {five}")


