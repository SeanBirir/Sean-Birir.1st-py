"""Function , collection of code that performs a specific task.
Functions allow you to organise your code alot better"""
#Creating a function thatsays hi to the user using def.
#The code that goes inside of a function needs to be indented.

def say_hi():
    print("Hello user")

say_hi()

#Parameter , a piece of information given to the function.

def say_hi(name):
    print("Hello " + name )

say_hi("Sean")
say_hi("John ")

#can put more han one piece of information.
def say_hi(name ,age):
    print("Hello " + name + " you are " + age + " years old.")

say_hi("Sean","20")
say_hi("John","30")