#simple calculator in Python

#Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")

#Perform the calculation based on the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operation."

    #Display the result
print("Result:", result)
# End of calculations.py




