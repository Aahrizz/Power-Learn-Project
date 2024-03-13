#def outer_fun(a, b):
 #   def inner_fun(c, d):
  #      return c + d
 #return inner_fun(a, b)

#res = outer_fun(5, 10)
#print(res)

#def add(a, b):
 #   return a+5, b+5

#result = add(3, 2)
#print(result)

#for num in range(1, 5):
 #   print(num)

#x = 0 
#for i in range(3):
 #   x = x + i
    
#print(x)

list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum = 0
sum1 = 0
for elem in list1:
    if (elem % 2 == 0):
        sum = sum + elem
        continue

    if (elem % 3 == 0):
        sum1 = sum1 + elem

print(sum , end=" ")