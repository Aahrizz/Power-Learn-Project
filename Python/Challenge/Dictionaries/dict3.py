#prevent duplication of keys
user_dict = {}
max_length = 3

while len(user_dict) < max_length:
    name = input("Enter employee's name: ")
    salary = input("Enter employee's salary: ")

    if name not in user_dict:
        user_dict[name] = salary

print("Final dictionary:", user_dict)
