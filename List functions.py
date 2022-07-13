#This functions helps us to modify the lists and get information about the lists.
#Extend function , allows us to append another list to an already existing list

from copy import copy
from numpy import insert

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.extend(Lucky_numbers)

print(friends)

#Append, allows me to add another item to the end of the list.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.append("Jeniffer")

print(friends)

#insert, allows me to add an item in the middle of the list.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.insert(1,"Jeniffer")

print(friends)

#Remove ,allows me to remove an item from the list.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Jeniffer","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.remove("Jeniffer")

print(friends)

#Clear, it will remove everything from the list.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.clear()

print(friends)

#pop ,it gets rid of the last element in the list.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.pop()

print(friends)

#index, will show you the index of the searched item.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]

print(friends.index("Ross"))

#Count, counts the total numer of similar items in the list.

Lucky_numbers =[3,45,6,15,6,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe","Phoebe"]

print(friends.count("Phoebe"))

#sort, puts the list in alphabetical order,and numbers on ascending order

Lucky_numbers =[3,45,6,15,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.sort()
Lucky_numbers.sort()

print(friends)
print(Lucky_numbers)

#reverse, reverses the list.

Lucky_numbers =[3,45,6,15,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends.reverse()
Lucky_numbers.reverse()

print(friends)
print(Lucky_numbers)

#copy,create another list and set it as a copy.

Lucky_numbers =[3,45,6,15,43,5,]
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]

friends2 = friends.copy()
Lucky_numbers2 = Lucky_numbers.copy()

print(friends2)
print(Lucky_numbers2)