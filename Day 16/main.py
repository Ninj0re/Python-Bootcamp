from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    choice = input("What would you like to order (" + menu.get_items() + ") ")
    if choice == "off":
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    drink = menu.find_drink(choice)
    if drink is None:
        continue
    if coffee_maker.is_resource_sufficient(drink):
        print(f"Insert {drink.cost}$")
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
