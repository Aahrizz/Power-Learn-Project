#initialize an empty dict
users = {}

#initialize an entry count for keys to make
user_entries = int((input("Enter number of entries you want to make: ")))

#loop thru the entry count
for i in range(user_entries):
    key = input(f"Enter key name {i + 1}: ")
    value = input(f"Enter value {i + 1}: ")
    users.update({key : value})#use of update method

print(users)