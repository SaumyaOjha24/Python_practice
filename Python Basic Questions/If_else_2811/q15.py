# Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
# for Monday, 2 for Tuesday, etc.).

day = int(input("Enter a number (1-7): "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= day <= 7:
    print(days[day-1])
else:
    print("Invalid input")
