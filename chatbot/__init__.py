from payment import PaymentMethod
from .order import Order
from shop import shop_items
import inquirer
from decimal import Decimal


def handle_customer_order(order: Order):
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
            choices=[
                "Add item to order",
                "Remove item from order",
                "Browse",
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
        case "Browse":
            handle_browse_shop()
        case "Show cart":
            handle_show_cart(order)
        case "Checkout":
            if handle_checkout_order(order):
                return False
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
            validate=lambda _, answer: answer.isdigit() and int(answer) >= 0,
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
            validate=lambda _, answer: answer.isdigit() and int(answer) >= 0,
        ),
    ]
    answers = inquirer.prompt(questions)
    order.remove_from_order(answers["item"], int(answers["quantity"]))


def handle_browse_shop():
    print("These are our items:\n")
    for item in shop_items.values():
        print(item)


def handle_checkout_order(order: Order):
    questions = [
        inquirer.List(
            "confirm",
            message="Are you sure?",
            choices=[
                ("Yes", True),
                ("No, keep shopping", False),
            ],
        ),
        inquirer.List(
            "payment_method",
            message="How would you be paying today?",
            choices=[
                (PaymentMethod.CREDIT_CARD.value, PaymentMethod.CREDIT_CARD),
                (PaymentMethod.CASH.value, PaymentMethod.CASH),
            ],
            ignore=lambda answers: answers["confirm"] is False,
        ),
        inquirer.Text(
            "cash",
            message="Please enter your cash amount.",
            ignore=lambda answers: answers["payment_method"] is None
            or answers["payment_method"] == PaymentMethod.CREDIT_CARD,
            validate=lambda _, answer: (value := answer.replace(".", "", 1))
            and (value.isdigit())
            and int(value) >= 0,
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["confirm"]:
        return order.checkout(
            answer["payment_method"], Decimal(answer.get("cash") or 0)
        )
    return False


def handle_show_cart(order: Order):
    order.display_order()
