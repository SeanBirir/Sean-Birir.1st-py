#strings

"""you can create a new line in a string,just by using backslash and  an n after it.
and to print a quotation mark as an output ,use backslash and add the quotation marks after """

print("1 Python Strings")
print("2 python Strings")
print("3 python Strings")

#you can create a string variable

phrase = "Python Strings through Variable"
print(phrase)

#concatenation

"""you can actually use concatenation to add a string to another string"""
print(phrase + " and with Concatenation")

#turn a whole string to lower case letters using .lower()

print("LOWER CASE".lower())
print(phrase.lower())

#turn a whole string to uper case letters using .upper()

print("upper case".upper())
print(phrase.upper())

#checking if string is in uppercase or lowercase using .isupper() or .islower()

print("LOWER CASE".islower())
print("upper case".isupper())
print("LOWER CASE".isupper())
print("upper case".islower())

#you can combine the two and get a fixed upercase or lowercase

print("LOWER CASE".lower().islower())
print("upper case".upper().isupper())

#figuring out how many characters are in a string usin (len())

print(len(phrase))

"""to print out a single character in a string using [index of the string]
an index in python starts its first charactr at index 0"""

print(phrase[0])

#figuring out where  a chatacter is located in a string, or even more than one character using .index("the character")

print(phrase.index("P"))
print(phrase.index("Strings"))

#replacing characters in strings using .replace("characters","replacement")

print(phrase.replace("Strings","replacement"))



