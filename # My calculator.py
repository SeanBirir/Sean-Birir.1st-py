#I am building a simple calculator using the different functions

from pdb import Restart

from pip import main

print("Enter your first number, second number and finally the operation you want to use to do the calculation.")
print("you can use a decimal number.")
print("Type in (yes) to continue calculating if you want when done.")

def main() : 

    num1 = float(input("Enter the first number : "))
    op = input("Enter operater :")
    num2 = float(input("Enter the second number : "))

    try :

        if op =="+" :
            print(num1 + num2)
        elif op =="-" :
            print(num1 - num2)  
        elif op == "/" :
            print(num1 / num2)
        elif op == "*"  :
            print(num1 * num2)  
        elif op == "^" :
            print(num1 ** num2)

    except ZeroDivisionError as error:
        print(error)

    except:    
        print("Sorry,there is an error in your input.")

    Restart=input("Do you still want to calculate ? ")

    if Restart == "yes":
        main()

    else:
        print("End of the calculation.") 
main()


