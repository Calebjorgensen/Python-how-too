#This is all about lists.


#As you can see the list stores the valves.
cart = ["milk", "tea", "juice", "apple"]
print(cart)


#With this example you can see that the list can store different types. 
movie_info = ["inception", 2010]
print(movie_info)

#Some lists can be long so you can place them on different lines
movie_collection = [
    "Thor",
    "Iron Man",
    "Star Wars",
    "Inception",
    "Shark Tales"
]
print(movie_collection)

#All lista have an index number. Its how we or the computer can keep track of the different items.
#Its important to remember that when we count in programming we start at 0 not 1.
#So if we want to access value in a list we use its index.


#So for this list spiderman is 0, superman is 1 and the list continues to count up from there. 
heros = ["Spiderman", "Superman", "Iron Man", "Hulk", "Thor", "Hawkeye", "Black Widow", "Captian America"]
print(heros[1])

favorite_hero = heros[0]
print(favorite_hero)


#You can use the indexs to just grab some of the values.
#The starting index is inclusive and the stopping index is exclusive. 
print(heros[0:1])

#This one will index all values up to 4
print(heros[:4])

#This one will index all values after 2
print(heros[2:])

#This is one is a negative index, these 2 print statements return the same value. negative index work right to left from the list.
#But for negative it starts at -1 not zero. 
print(heros[-1])
print(heros[7])

#Another example of negative index
print(heros[-3:-1])

print(heros[1:-1])



# choice = int(input("Which is your favorite hero: "))

# print(heros[choice])

