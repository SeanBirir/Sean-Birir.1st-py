"""I will get two numbers from the user using the input() method and 
put them in variables to create my calculator."""

print("The numbers you input are going to be added together in different ways.")
num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = num1 + num2

print(result)

"""It is going to print out the wrong answer because python will automaically put the users input as a sring
So i am going to convert them from strings to numbers using these funcions"""
#int(num1) + int(num2),which does not use decimals.

print("Do not insert decimal numbers in the next addition.")
num1 = input("Using int-Enter a number:")
num2 = input("Using int-Enter another number:")
result = int(num1) +int(num2)

print(result)

#Float, which uses a number that has decimals or a whole number.

print("You can insert any number.(even a decimal number).")
num1 = input("Using float-Enter a number:")
num2 = input("Using float-Enter another number:")
result = float(num1) +float(num2)

print(result)
print("The end")