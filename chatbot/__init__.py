from .order import Order
from shop import shop_items
import inquirer


def handle_customer_order(order: Order):
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
            choices=[
                "Add item to order",
                "Remove item from order",
                "Show cart",
                "Checkout",
                "Quit",
            ],
        )
    ]
    answers = inquirer.prompt(questions)
    match answers["action"]:
        case "Add item to order":
            handle_add_item_to_order(order)
        case "Remove item from order":
            if next(iter(order), None) is None:
                print("Your cart is empty.")
            else:
                handle_remove_item_from_order(order)
        case "Show cart":
            handle_show_cart(order)
        case "Checkout":
            return handle_checkout_order(order)
        case "Quit":
            return False
    return True


def handle_add_item_to_order(order: Order):
    questions = [
        inquirer.List(
            "item",
            message="What item would you like to add?",
            carousel=True,
            choices=[(item.name, item) for item in shop_items.values()],
        ),
        inquirer.Text(
            "quantity",
            message="How many would you like to add?",
            validate=lambda _, answer: answer.isdigit() and int(answer) > 0,
        ),
    ]
    answers = inquirer.prompt(questions)
    order.add_to_order(answers["item"], int(answers["quantity"]))


def handle_remove_item_from_order(order: Order):
    questions = [
        inquirer.List(
            "item",
            message="What item would you like to remove?",
            choices=[(f"{item.name}({count})", item) for (item, count) in order],
        ),
        inquirer.Text(
            "quantity",
            message="How many would you like to remove?",
            validate=lambda _, answer: answer.isdigit() and int(answer) > 0,
        ),
    ]
    answers = inquirer.prompt(questions)
    order.remove_from_order(answers["item"], int(answers["quantity"]))


def handle_checkout_order(order: Order):
    order.checkout()


def handle_show_cart(order: Order):
    order.display_order()
