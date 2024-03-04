#similar to lists but immutable after creation
#parenthesis optional, elements seprated by commas

places = ("kenol",) #tuple with one element
print(type(places))
print(places)


languages = ("creole", "swahili", "amhara", "mandarin")
for language in languages:
    print("My favorite language is: ", language)

#accessing tuples
g6 = "Kenya", "Ethiopia", "Rwanda", "Sudan", "Uganda", "Tanzania"
g6 = "Kenya", "Ethiopia", "Rwanda", "Sudan", "Uganda" 

print(g6)
print(type(g6))

print(g6[-1])
print(g6.count("a"))

