# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.


# Simple calculator program

# Function to perform the arithmetic operations
def calculator(num1, num2, operation):
    if operation == '1':  # Addition
        return num1 + num2
    elif operation == '2':  # Subtraction
        return num1 - num2
    elif operation == '3':  # Multiplication
        return num1 * num2
    elif operation == '4':  # Division
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Main program
print("Simple Calculator")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Taking user inputs
operation_choice = input("Enter the number of the operation (1/2/3/4): ")

# Input numbers
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Perform the calculation
    result = calculator(number1, number2, operation_choice)

    # Display the result
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
