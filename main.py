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

def report():
    print(resources)

def is_resources_sufficient():
    if user_input=="espresso":
        if resources["water"] > 50 and resources["milk"] > 0 and resources["coffee"] > 18:
            return True
        else:
            return False
    elif user_input=="latte":
        if resources["water"] > 200 and resources["milk"] > 150 and resources["coffee"] > 24:
            return True
        else:
            return False
    elif user_input=="cappuccino":
        if resources["water"] > 250 and resources["milk"] > 100 and resources["coffee"] > 24:
            return True
        else:
            return False
        
def process_coins():
    quarters = float(input("how many quarters?: ")) *0.25
    dimes = float(input("how many dimes?: ")) *0.1
    nickles = float(input("how many nickles?: ")) *0.05
    pennies = float(input("how many pennies?: ")) *0.01
    sum = quarters + dimes + nickles + pennies
    return sum

def change(money,cost):
    change1 = money-cost
    change1 = round(change1)
    print(f"here is your change: ${change1}")

user_input = input("what would you like? (espresso/latte/cappuccino)")
game_on = True

if user_input=="off":
    pass
elif user_input == "report":
    report()
elif user_input=="latte" or user_input=="espresso" or user_input=="cappuccino":
    if is_resources_sufficient():
        newsum = process_coins()
        if user_input=="latte":
            if newsum > MENU["latte"]["cost"]:
                print("here is your latte sir")
                change(newsum,MENU["latte"]["cost"])
            else:
                print("sorry that's not enough money. Money refunded")
        elif user_input=="espresso":
            if newsum > MENU["espresso"]['cost']:
                print("here is your espresso")
                change(newsum,MENU["espresso"]['cost'])
            else:
                print("sorry that's not enough money. Money refunded")
        elif user_input=="cappuccino":
            if newsum > MENU["cappuccino"]['cost']:
                print("here is your cappuccino sir")
                change(newsum,MENU["cappuccino"]['cost'])
            else:
                print("sorry that's not enough money. Money refunded")
    else:
        print("not enough resources")

    