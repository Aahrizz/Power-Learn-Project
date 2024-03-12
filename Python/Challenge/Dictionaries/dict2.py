#use of compression method
user_entries = int(input("How many entries do you wanna make: "))

users = {input(f"Enter key name {i + 1}: "): input(f"Enter value {i + 1}: ")
    for i in range(user_entries)
}

print(users)

