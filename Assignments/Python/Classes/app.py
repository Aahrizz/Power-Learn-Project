inval=int(input('Input an integer greater than 5 and less than or equal to 10: '))
# your code goes here
if 5 < inval <= 10:
    for inval in range (0, inval+1):
        print(inval)
        if (inval * 10 ) > 70:
            
            break
else:
    print('You did not enter a value between 1 and 5')