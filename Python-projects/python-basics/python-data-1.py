#python-data-1 is the first in a series that will go through syntax and the basics of python coding language!
print("Hello, World!")
#The print function is used to print data to the console. 
#Its how to output data to the user.
print()
#You can use an empty print function to print a new line.
#There will be multiple empty print functions in the code to make the output more readable.


# The # is used to make a comment in python. The purpose of a comment is to explain the code, but it is not executed by the computer.


#Variables.
first_name = "John"
last_name = "Doe"
#Variables are used to store data in a program.
print(first_name, last_name)
print()

#Data types are the type of data that a variable can store.
#There are many data types in python, but the most common are:
#String: A string is a sequence of characters.
#Integer: An integer is a whole number.
#Float: A float is a decimal number.
#Boolean: A boolean is a True or False value.
#List: A list is a collection of items.
#Dictionary: A dictionary is a collection of key-value pairs.
#Tuple: A tuple is an immutable sequence of items.

#Strings are sequences of characters.
test_string = "Hello World!"

#Integers are whole numbers.
test_integer = 10

#Floats are decimal numbers.
test_float = 10.5

#Booleans are True or False values.
test_boolean = True
# Important thing to note about booleans, if you set a variable as a boolean remember to capitalize the first letter. Python is case-sensitive.

#Lists are collections of items.


#Dictionaries are collections of key-value pairs.


#Tuples are immutable sequences of items.

#Variables can also store data from the user.
name = input("What is your name? ")
print("Hello, " + name + "!")
print()
#This is an example of getting an input from the user and then outputting that data. 
#Example of this is when you sign up for a new service, you might put in your name, age, email and the service can start outputting some of that data.

#Another example.
age = input("What is your age? ")
print("Your age is " + age)
#This example brings up a question. We are asking for the users age, which most people will interpret that data we get is going to be an integer. 
#But how do we know what type of data the computer stored it as? Well there is a syntax to find out.
print(type(age))
#If you run the program with this type you will see it return a <class 'str'> meaning it stored the age type as a string not an integer. 
#Thats not a problem for this example but what if you wanted to build a calculator app what would happen?

#You can do simple functions with certain syntax, like add, substract, multiple, or devide. 
#Let me show you some examples before I answer the problem above. 
print()
math1 = 3
math2 = 6
print(math1 + math2)