"""we can make a more advanced calculator using the if statements,
combining with the input function and float function to turn them from srteings to real numbers."""

num1 = float(input("enter first number :"))
op = input("Enter operater :")
num2 = float(input("enter second number :"))

if op =="+" :
    print(num1 + num2)
elif op =="-" :
    print(num1 - num2)  
elif op == "/" :
    print(num1 / num2)
elif op == "*"  :
    print(num1 * num2)  
else:
    print("Invalid operator.")
    