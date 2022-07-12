"""Numbers can be printed out without using the quotation marks
It also applies to decimals and also negative numbers"""

print(20)
print(20.011)
print(-20)

"""It is also posssible to do basic arithmetics like, 
Addiion(+),Subraction(-),Division(/) and Multiplicaion"""

print(20 + 5.5)
print(20 - 5.5)
print(20 / 5.5)
print(20 * 5.5)

#Even complex mathematical equations ,python specifies order of operations.Even brackets are used in the order.

print(20 * 5.5 + 0.5)
print(20 * (5.5 + 0.5))

"""we can use an operator called Modulus operator(%) 
I basically divides two numbers and prints out the remainder"""

print(10 % 3)

"""these numbers can be stored in variables nd they can be converted to a string
It is not going to allow concantation unless it is a string,
so i is important to change a number to a sring"""

my_num = 10
print(my_num)
print(str(my_num))
print(str(my_num) + " is my favorite number")

#Common functions
#absolute value(abs),this will just give the absolute value of the number

my_num = -10
print(abs(my_num))

#pow,used to take a number to a cerain power like (3 power 2 = 9)

my_num = 10
print(pow(3 , 2))
print(pow(my_num , 2))

#Max ,shows which of the numbers is higher

print(max(3 , 2))
print(max(my_num , 2))

#Min ,shows which of the numbers is Lower

print(min(3 , 2))
print(min(my_num , 2))

#round , it is going to round  a number o nearest whole number

print(round(20.54567))

#To get access to more functions,you have to import an externl code to the file
#floor , i is going to chop off the lowest number

from math import *

my_num = -10
print(floor(20.7))

#ceil,i is going to round UP a number no matter the value of the decimal

print(ceil(20.7))
print(ceil(20.2))

#sqrt ,just returns squae root of a number

print(sqrt(81))
print(sqrt(100))



