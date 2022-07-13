"""If statements allow our programs to respond to the input they are given,
which means the program is going to make decisions."""
#creating a boolean variable, it is only going to print if it is true.

is_male = True

if is_male:
    print("you are a male")

#else,is used to show otherwise
#or,is used if one or both of the values are true.

is_male = True
is_tall = True

if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("you neither not a male nor tall")    

#and ,both conditions have to be true

is_male = True
is_tall = True

if is_male or is_tall:
    print("you are a tall male")
else:
    print("you  not male or tall or both") 

    #use elif you can put another condition.

is_male = True
is_tall = True

if is_male or is_tall:
    print("you are a tall male.")
elif is_male and not (is_tall):
    print("you are a short male.")  
elif not is_male and (is_tall):
    print("you are not a male but tall.")      
else:
    print("you not male and tall.")