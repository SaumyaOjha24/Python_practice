# Q11 Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.

price = float(input("Enter product price: "))

if price > 1000:
    discount = 0.10
elif price >= 500:
    discount = 0.05
else:
    discount = 0

final_price = price - (price * discount)

print("Final Price:", final_price)
