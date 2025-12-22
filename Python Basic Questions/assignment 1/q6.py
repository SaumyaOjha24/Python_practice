"""Q6 Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and
performs the specified operation. Print the result based on the operation."""

a = float(input("First: "))
b = float(input("Second: "))
op = input("Op: ")

if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/' and b != 0: print(a / b)
elif op == '/': print("Cannot divide by zero")
else: print("Invalid")