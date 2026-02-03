#Loops

# For loops

for i in range(5):
    print("Hello world!")

print()

for x in range(10):
    print(x)

print()

for i in range(3):
    print(i < 1)

print()


#While loops repeat code whilst a condition holds.
# While loops
seats = 15 #Variable
while seats > 0: #the while start
    print("Sell tickets")
    seats = seats -1 # this is the counter or the updated variable


print()

timer = int(input("Please enter an amount of seconds: "))
while timer > -1:
    print(timer)
    timer = timer -1


print()

cells = int(input("How many cells did you start with: "))

days = int(input("How many days did you let them grow: "))

counter = 1

while counter <= days:
    cells = cells * 2
    print("Day " + str(counter) + ": " + str(cells))
    counter = counter + 1