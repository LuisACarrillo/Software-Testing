# 3. Function that calculates the discount for a customer's purchase based on the total amount.
# The discount rules are as follows:

# If the total amount is less than 100, no discount is applied.
# If the total amount is between 100 and 500 (inclusive), a 10% discount is applied.
# If the total amount is greater than 500, a 20% discount is applied.

# calculate_discount(purchase)
# purchase is not a number
#     return
# purchase < 0
#     return
# purchase < 100
#   return purchase
# 100 <= purchase <= 500
#   purchase = purchase * 0.9
# purchase > 500
#   purchase = purchase * 0.8

# print(calculate_discount(50))    
# print(calculate_discount(150))  
# print(calculate_discount(600))  
# print(calculate_discount(-10))  
# print(calculate_discount("abc")) 
# print(calculate_discount(0.1))
# print(calculate_discount(1000000000000))
# print(calculate_discount(-1000000000000))

def calculate_discount(purchase):
    if isinstance(purchase, (int, float)) is False:
        return
    if purchase < 0:
        return
    if purchase < 100:
        return purchase
    elif 100 <= purchase <= 500:
        return purchase * 0.9
    else: 
        return purchase * 0.8
    
# Example usage:
print(calculate_discount(50))    
print(calculate_discount(150))  
print(calculate_discount(600))  
print(calculate_discount(-10))  
print(calculate_discount("abc")) 
print(calculate_discount(0.1))
print(calculate_discount(1000000000000))
print(calculate_discount(-1000000000000))
