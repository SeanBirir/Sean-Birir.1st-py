#continuation from (reading files.py).
#"a"(append)-means you can append more information to the end of the existing information and nothing else

first_test_file = open("first test.txt","a")

first_test_file.write("kelly->member")

first_test_file.close()

#"w"(write)-will allow you to add new information and change existing information.
#you can use it to create new files.

first_test_file = open("first test 2.txt","w")

first_test_file.write("kelly->member")

first_test_file.close()