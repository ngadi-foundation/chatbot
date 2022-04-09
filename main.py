# coding: utf8
from shop import shop_items
from chatbot import handle_customer_order, Order


def welcome_message():
    print("Welcome to Bob's carptentary shop!")


def main():
    welcome_message()
    order = Order()
    while handle_customer_order(order):
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()
