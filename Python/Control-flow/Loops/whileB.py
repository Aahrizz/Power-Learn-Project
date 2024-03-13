food = ["ugali", "chapati", ["smocha, juice"], "mala", "beef"]

best = ["smocha, juice"]

length = len(food)
count = 0

while (count < length):
    print(food[count])
    
    if food[count] == best:
        print("They have what I desire")
        break
    count += 1