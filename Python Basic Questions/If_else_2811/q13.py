# Q13 Write a program that simulates a simple ATM. The user should be able to:
# Check balance
# Deposit money
# Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices.

balance = 5000  # initial balance

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful")
    print("Updated balance:", balance)

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful")
        print("Updated balance:", balance)
    else:
        print("Insufficient balance")

else:
    print("Invalid choice")
