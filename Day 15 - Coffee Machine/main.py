"""Coffee machine program"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources: dict[str, int] = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

collected_amount = 0
is_on = True

def make_coffee(drink_name, order_ingredients):
    """Deduct quantity from the available resources and make coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} Enjoy!!")

def is_resource_sufficient(order_ingredients):
    """Returns True if the resources are sufficient, else False."""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters_value = int(input("How many quarters?: "))
    dimes_value = int(input("How many dimes?: "))
    nickles_value = int(input("How many nickles?: "))
    pennies_value = int(input("How many pennies?: "))
    total_money_provided = round((0.25 * quarters_value) + (0.10 * dimes_value) + (0.05 * nickles_value) + (0.01 * pennies_value), 2)
    return total_money_provided

def is_transaction_successful(coffee_request, drink, total_money_provided):
    """Return True when the payment is successful, or False is money is insufficient."""
    if total_money_provided >= drink["cost"]:
        change = round(total_money_provided-drink['cost'], 2)
        print(f"Here is your ${change} in change.")
        global collected_amount
        collected_amount += drink["cost"]
        return True
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False

while is_on:
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    coffee_request = input("What would you like? (espresso/latte/cappucino): ")

    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee_request == "off":
        is_on = False
    # 3. Print report.
    elif coffee_request == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${collected_amount}")
    else:
        # 4. Check resources sufficient?
        drink = MENU[coffee_request]
                        
        if is_resource_sufficient(drink["ingredients"]):
            # 5. Process coins.
            total_money_provided = process_coins()
            # 6. Check if transaction is successful
            if is_transaction_successful(coffee_request, drink, total_money_provided):
                # 7. Deduct resources and make coffee
                make_coffee(coffee_request, drink["ingredients"])
