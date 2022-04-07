# coding: utf8
from shop import shop_items
from chatbot import handle_customer_order, Order


def welcome_message():
    print("Welcome to Bob's carptentary shop!")


def display_shop_items():
    print("These are our items:\n")
    for item in shop_items.values():
        print(item)


def main():
    welcome_message()
    display_shop_items()
    order = Order()
    while handle_customer_order(order):
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()
