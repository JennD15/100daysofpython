from coffee_data import MENU
from coffee_data import resources

profit = 0
espresso = MENU["espresso"]["ingredients"]
latte = MENU["latte"]["ingredients"]
cappuccino = MENU["cappuccino"]["ingredients"]
espresso_price = 1.50
latte_price = 2.50
cappuccino_price = 3.00


# dictionary that stores the monetary value of the coins
monetary_value ={
    "quarter" : 0.25, 
    "dime" : 0.10,
   "nickel" : 0.05,
    "penny" : 0.01,
}


def coffee_flavor(choice):
    """function that will take input and return ingredients"""
    if choice == 'espresso':
        return espresso
    elif choice == 'latte':
        return latte
    elif choice == 'cappuccino':
        return cappuccino
     

def total_amount(choice):
    """function that will return the amount to pay"""
    if choice == 'espresso':
       return espresso_price
    elif choice == 'latte':
        return latte_price
    elif choice == 'cappuccino':
        return cappuccino_price


def check_resources():
    coffee_ingredients = coffee_flavor(choice)
    is_enough = True
    for item in coffee_ingredients:
        if coffee_ingredients >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            is_enough = False
    return is_enough

# function that will check if transaction is successful
def money_inserted():
    """function that will take the input of the amount of coins inserted and calculate the total"""
    profit = 0
    quarters = int(input("How many quarters? ")) * monetary_value["quarter"]
    dimes = int(input("How many dimes? ")) * monetary_value["dime"]
    nickels = int(input("How many nickels? ")) * monetary_value["nickel"]
    pennies = int(input ("How many pennies? ")) * monetary_value ["penny"]
    total = ("{:.2f}".format(quarters + dimes + nickels + pennies))
    if total < total_price:
        print("Sorry that's not enough money. Money refunded.")
    elif total > total_price:
        change = "{:.2f}".format( float(total) - float(total_price))
        print(f"Here is {change} dollars in change")
    elif total == total_price:
        profit += float(total)
        print(profit)




is_on = True

while is_on:
   
    choice = input("What would you like? 'espresso', 'latte', or 'cappuccino' ")
    if choice == 'report':
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} ml")
        print(f"money: {profit}")
    elif choice == 'off':
        is_on = False
    else:
        check_resources()
        total_price = "{:.2f}".format(total_amount(choice))
        print(f"You're total is {total_price} Please insert coins ")
        money_inserted()






    













# function that will check if resources are sufficient



