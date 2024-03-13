nums = [4, -11, 69, 53, -65]
doubled = []

for num in nums:
    doubled.append(num * 2)
print(doubled)

#same code but in one line
namba = [21, -98, 9, -33, 7]

jumlisha = [nambari * 2 for nambari in namba]
print(jumlisha)

#syntax for list comprehension
#new-list = [<expression> for <element> in <collection>]