"""Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
on the following criteria:
>= 90: Grade A
>= 80: Grade B
>= 70: Grade C
>= 60: Grade D
< 60: Grade F"""

grade=int(input("give the grade: "))
if grade>=90:
    print("grade A")
elif grade>=80:
    print("grade B")
elif grade>=70:
    print("grade C")
elif grade>=60:
    print("grade D")
else:
    print("grade F")
