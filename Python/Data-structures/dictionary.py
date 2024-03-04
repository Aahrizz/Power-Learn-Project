#ordered collection of items
#includes key value pair

capitalCities = {"Kenya" : "Nairobi", "Uganda" : "Kampala", "Tanzania" : "Dodoma"}
t = type(capitalCities)

##for order in capitalCities:
    ##for value in  order:
        ##print(order, value)
    #print(order)
print(t)

results = {1 : "kiptum", 2 : "Kiptoo", 3 : "jepngetich"}
print(results)

#add a key value pair
results[4] = "Nyashinski"
print(results)

#change & remove value
del results[3]
print("New results: ", results)

results[4] = "Rudisha"
print(results)

#access the values
print(results[1])

#remove the whole dict using del keyword
names = {"A" : "amos", "B" : "beta", "C" : "chord"}
print(names)
#del names
#print(names)

#Dict methods

Wins = {1 : "kiptum", 2 : "Kiptoo", 3 : "jepngetich"}
#all() 
print(all(Wins))#True if dict empty or values are True

#any()
print(any(Wins))#true if any value is true, false if dict is empty
lies = {}
print(any(lies))

#len
length = len(Wins) #returns number of items in the dict
print(length)

#sorted()
new = sorted(Wins)
print(new)

#clear
#removes all items from the dict
fruit_prices = {
    "apple": 1.0,
    "banana": 0.6,
    "orange": 0.8,
    "grape": 1.2
}

print("apple" in fruit_prices)
print("kiwi" in fruit_prices)

for i in fruit_prices:
    print(i, fruit_prices[i])