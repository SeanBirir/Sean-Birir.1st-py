"""you can open an external file in python.
when you add: 
"r"(read)-it will only allow you to read te file and nothing else
"w"(write)-will allow you to add new information and change existing information.
"a"(append)-means you can append more information to the end of the existing information and nothing else
"r+"(read and write)-you can both read and write.
-always close the file after- """
#you can check if the file is readable first.

first_test_file = open("first test.txt","r")

print(first_test_file.readable())

first_test_file.close()

#I will be reading from the file.

first_test_file = open("first test.txt","r")

print(first_test_file.read())

first_test_file.close()

#you can even read from a individual line in order using .readline().

first_test_file = open("first test.txt","r")

print(first_test_file.readline())
print(first_test_file.readline())
print(first_test_file.readline())
print(first_test_file.readline())

first_test_file.close()

#i can even put the lines in a list using .radlines()

first_test_file = open("first test.txt","r")

print(first_test_file.readlines())

first_test_file.close()

#I can also create the .readlines() with a for loop

first_test_file = open("first test.txt","r")
for first_test in first_test_file.readlines():
    print(first_test)
first_test_file.close()