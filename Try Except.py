"""Try except, prevents your program to stop working because of a wrong input.
like for example where you are supposed to input an integer but you input a letter,
the program will print out a message that the creator created and the program will continue normally."""

from numpy import number

try:
    number =int(input("Enter mumber :"))
    print()
except:
    print("Invalid input!")    

#we can put more than one except,and also sore them in variables.

try:
    number =int(input("Enter mumber :"))
    print()
except ZeroDivisionError as error:
    print(error)
except:    
    print("Invalid input!")