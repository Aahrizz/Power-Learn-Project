def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        price
    
original_price = float(input())
discount_percentage = float(input())
final_price = calculate_discount(original_price, discount_percentage)
print(f"Original Price: ${original_price:.2f}")
print(f"Discounted Price: ${final_price:.2f}")
