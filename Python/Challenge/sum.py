#create an empty list to store our integers
nums =[]

#prompt for a list of integers
n = int(input("Enter number of integers: "))

#loop through a defined range of number(s) 
for i in range(n):
    integers = int(input(f"Enter integer {i + 1}: "))#stores our numbers while increasing our range count by one
    nums.append(integers)# appends the integers to our empty list

print(nums)#output of the final list
sum = 0#initialize the sum of intergers at 0

#loops through the list
for i in nums:
    sum += i
print(sum)#output of the sum