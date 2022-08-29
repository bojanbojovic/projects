from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

toContinue = True

while toContinue:
    order = input("What would you like? (espresso/ latte/ cappuccino): ")

    if order == "off":
        break

    if order == "report":
        coffee_maker.report()
        money_machine.report()

    if order == "espresso":
        espresso = menu.find_drink("espresso")
        if coffee_maker.is_resource_sufficient(espresso):
            if money_machine.make_payment(1.5):
                coffee_maker.make_coffee(espresso)
    elif order == "latte":
        latte = menu.find_drink("latte")
        if coffee_maker.is_resource_sufficient(latte):
            if money_machine.make_payment(2.5):
                coffee_maker.make_coffee(latte)
    elif order == "cappuccino":
        cappuccino = menu.find_drink("cappuccino")
        if coffee_maker.is_resource_sufficient(cappuccino):
            if money_machine.make_payment(3.0):
                coffee_maker.make_coffee(cappuccino)
