# Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
# triangle. A triangle is valid if the sum of any two sides is greater than the third side.
# Check conditions like a + b > c, b + c > a, and a + c > b.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and b + c > a and a + c > b:
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")
