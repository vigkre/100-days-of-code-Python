"""Pizza Deliveries Program"""

print("Welcome to the Python Pizza Deliveries!")
size = input("What size of Pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_for_small_price = 2
pepperoni_for_others_price = 3
extra_cheese_price = 1
final_bill = 0
if size == "S":
    final_bill = small_pizza_price
elif size == "M":
    final_bill = medium_pizza_price
elif size == "L":
    final_bill = large_pizza_price
else:
    print("You typed wrong size, please choose S, M or L !!!")

if pepperoni == "Y":
    if size == "S":
        final_bill += pepperoni_for_small_price
    else:
        final_bill += pepperoni_for_others_price

if extra_cheese == "Y":
    final_bill += extra_cheese_price


print(f"Your final bill is: ${final_bill}")
