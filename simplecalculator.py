#Addition
def add(m, n):
    return m + n

#Subtraction
def subtract(m, n):
    return m -n

 #Multiplication
def multiply(m, n):
    return m * n

#Division
def divide(m, n):
    if n != 0:
        return m / n
    else:
        return "Cannot divide by zero"
#Power
def power(m, n):
    return m ** n

print("Simple Calculator")
print("Choose Operation you want to perform")
print("1. Addition ")
print("2. Subtraction ")
print("3.Multiplication ")
print("4. Division ")
print("5. Power ")
 
#Choose an Operation from choice
choice = input("Enter your choice (1/2/3/4/5): ")
 
#get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

 #Perform Calculation
result = 0
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
elif choice == '5':
    result = power(num1, num2)
else:
    print("Invalid choice.Please choose 1 or 2 or 3 or 4 or 5")


#Display Result
print(f"Result: {result}")     

