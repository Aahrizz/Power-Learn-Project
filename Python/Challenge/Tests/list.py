words = []

count = int(input("Enter count of words to write: "))

for i in range(count):
    word = input(f"Enter your word {i + 1}: ")
    words.append(word)
   
print(words)

oddWords = [wod for index, wod in enumerate (words)
    if index %2 != 0 ]

print(oddWords)
