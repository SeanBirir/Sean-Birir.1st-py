"""for loop allows us to loop over a collection of items,arrays, series of numbers...etc"""
#I will create a variable,and combine with for loop, .

from operator import index


for letter in "python":
    print(letter)

#using it on an array.print out a different value one by one.

friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
for character in friends :
    print(character)

#print out a range of numbers.


for index in range(10) :
    print(index)

for index in range(3,10) :
    print(index)

#we can do different things on the loop.

for index in range(5) :
    if index == 0:
        print("first")
    elif index == 1:
        print("second") 
    elif index == 2:
        print("third")    
    else:
        print("the rest")