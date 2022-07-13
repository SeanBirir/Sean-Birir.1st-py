#Lists are used to store lists of information to organise them and keep track of them for easier management.

friends =["Joey","Chandler","Rachel","Monica","Ross","Phoebe"]

print(friends)

"""The content in the lists have their own index positons.
and also access elements based on their index from the back of the list."""

friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]

print(friends[0])
print(friends[-1])

#you can also select more than one element in the list.
#Grabbing elements from a cerain index to the end of the list.

print(friends[1:])

#Grabbing elements between two chosen indexes.

print(friends[1:5])
print(friends[0:6])

#you can modify the list.
friends =["Joey","Chanler","Rachel","Monica","Ross","Phoebe"]
friends[1] = "Jeniffer"
print(friends[1])