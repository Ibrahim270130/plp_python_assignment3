def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    # If the discount is less than 20%, return the original price
    return price

# Prompt the user for the original price
price = float(input("Enter the original price of the item: "))

# Prompt the user for the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Call the calculate_discount function and store the result
final_price = calculate_discount(price, discount_percent)

# Print the final price
if final_price == price:
    print(f"No discount applied. The original price is: ${final_price}")
else:
    print(f"The final price after applying the discount is: ${final_price}")
