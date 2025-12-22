"""Q2 Write a program that takes three numbers as input and prints the largest of the three."""

a=int(input("enter number a: "))
b=int(input("enter number b: "))
c=int(input("enter number c: "))
if a>b and a>c:
    print(a,"is the greatest")
elif b>c:
    print(b,"is the greatest")
else:
    print(c,"is the greatest")
