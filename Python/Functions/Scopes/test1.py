#define a function to convert weight from pounds to kgs
def weight_converter(weight, conversion_rate):
    weight_in_kg = weight * conversion_rate
    return weight_in_kg

#prompts user to enter both the weight in pounds and rate used in conversion
weight_pounds = float(input())
rate = 0.453

#initialize a variable to store our function call with arguments as prompted values
weight_in_kg = weight_converter(weight_pounds, rate)
 
print(f"Weight in Pounds: {weight_pounds:.2f}")
print(f"Your weight in kgs: {weight_in_kg:.2f}")