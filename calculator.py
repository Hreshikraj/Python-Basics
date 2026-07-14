num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Choose operation (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Error: cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation"

print(f"Answer: {result}")
