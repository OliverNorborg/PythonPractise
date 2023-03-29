# Script for Day 15 - 100 days of python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}
profit = 0
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25 # Converting into dollars
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_resources_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def is_transaction_successfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is your chnage {change}")
        global profit
        profit += drink_cost
        return True
    else:
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ")

#print(MENU.keys())
#print(f"Cost of latte {MENU['latte']['cost']}")
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resource['water']}ml")
        print(f"Milk: {resource['milk']}ml")
        print(f"Coffee: {resource['coffee']}g")
        print(f"Profic: {profit}$")
    else:
        drink = MENU[choice]
        if is_resources_enough(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successfull(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
