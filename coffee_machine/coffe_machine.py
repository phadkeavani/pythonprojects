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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def make_a_coffee(coffee_name):
    coffee_tbd = MENU[coffee_name]["ingredients"]
    water = coffee_tbd["water"]
    if "milk" in coffee_tbd:
        milk = coffee_tbd["milk"]
    else:
        milk = 0
    coffee = coffee_tbd["coffee"]

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

def print_report():
    print("Resources Report")
    print(resources)

def check_if_enough_resources(coffee_name):
    coffee_tbd = MENU[coffee_name]["ingredients"]
    if resources["water"] > coffee_tbd["water"]:
        if "milk" not in coffee_tbd or resources["milk"] > coffee_tbd["milk"]:
            if resources["coffee"] > coffee_tbd["coffee"]:
                return "Yes"
            else:
                return "coffee"
        else:
            return "milk"
    else:
        return "water"
def calculate_money(q, d, n, p, c):
    coin_value = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    return round(coin_value - c, 2)


ready = True

while ready:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == 'off':
        ready = False
    if ready:
        if coffee_type == 'print report':
            print_report()
            continue
        #TODO 1: Check if coffe type is in the menu
        present = False
        for coffee in MENU:
            if coffee_type == coffee:
                present = True

        if present:
            # TODO 2 check if enough resources
            resources_present = check_if_enough_resources(coffee_type)
            if resources_present == 'Yes':
                # TODO 3 print cost of coffee and accept the coins
                cost = MENU[coffee_type]["cost"]
                print(f"Cost is {cost}")
                print("Please insert coins")
                try:
                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickles = int(input("How many nickles?: "))
                    pennies = int(input("How many pennies? :"))
                except ValueError:
                    print("Incorrect or no value entered!")
                    continue
                change_amt = calculate_money(quarters,dimes,nickles,pennies, cost)
                if change_amt < 0:
                    print("Sorry that's not enough money. Here's the refund, please try again!")
                else:
                    # TODO 4 Make a coffee
                    if change_amt == 0:
                        print("Exact amount paid!")
                    else:
                        print(f"Collect your change amount ${change_amt}")
                    make_a_coffee(coffee_type)
                    print("Enjoy your ☕")
            else:
                print(f"There is no enough {resources_present}. Please try again!")
        else:
            print("This coffee is not in menu!")




