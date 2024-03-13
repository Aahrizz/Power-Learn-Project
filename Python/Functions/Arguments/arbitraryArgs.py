#use (*) if unsure of numver of arguments to be passed in the function

def addNums(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

print(addNums(2,5,7,8,9,6,5,7))