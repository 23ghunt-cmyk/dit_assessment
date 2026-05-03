"""This is a pizza ordering system that allows customers to place pick up or deliver orders."""

# Imports
import os
import time

# Variables
ERROR_MESSAGE = "An error has occurred. Please enter a valid input"
DELIVERY_FEE = 10
MIN_PER_PIZZA = 15
LINE_WIDTH = 50

# List of pizza options:(Name, Small, Medium, Large)
PIZZA_MENU = [
    ["alphabet soup pizza", 10, 20, 30],
    ["hawian pizza", 10, 20, 30],
    ["meat lovers pizza", 10, 20, 30],
    ["margherita pizza", 10, 20, 30],
    ["pepperoni pizza", 10, 20, 30],
    ["gravel pizza", 10, 20, 30],
    ["baked bean pizza", 10, 20, 30],
    ["sushi", 10, 20, 30],
    ["mayonnaise", 10, 20, 30],
    ["escalator", 10, 20, 30],
    ["chair", 10, 20, 30],
    ["wood chunk", 10, 20, 30],
]


# Functions
def clear_screen():
    """Clear the terminal screen after a short delay."""
    time.sleep(0.9)
    os.system('cls')


def print_header(title):
    """Print a header."""
    print("\n" + "=" * LINE_WIDTH)
    print(f"{title.upper().center(LINE_WIDTH)}")
    print("=" * LINE_WIDTH)


def get_num(prompt_num):
    """Prompt user for a number and handle non integer input errors."""
    while True:
        try:
            num = int(input(prompt_num))
            return num
        except ValueError:
            print(ERROR_MESSAGE)


def pick_up():
    """Gather customer details for a pick up order and start the ordering process."""
    clear_screen()
    print_header("Pick Up Details")
    name = input("Name for Pick Up\n> ")
    phone_number = get_num("Phone number (no spaces)\n> ")
    process_order(name, "pick up", phone_number)


def delivery():
    """Gather customer details for a delivery order and start the ordering process."""
    clear_screen()
    print_header("Delivery Details")
    name = input("Name for Delivery\n> ")
    address = input("Address for Delivery\n> ")
    phone_number = get_num("Phone number\n> ")
    process_order(name, "delivery", phone_number, address)


def process_order(customer_name, order_type, phone, address="N/A"):
    """Manage the main pizza ordering loop, cart management, and receipt generation."""
    # Variables for order (not at top so they reset for each order)
    cart = []
    total = 0
    wait_time = 0

    while True:
        clear_screen()
        print_header("Menu")
        for item in PIZZA_MENU:
            print(f"{item[0]} | Small: ${item[1]} | Medium: ${item[2]} | Large: ${item[3]}")
        choice = input("Enter pizza name (type 'done' to finish)\n> ").lower().strip()
        if choice == "done":
            clear_screen()
            break

        found_pizza = None
        for item in PIZZA_MENU:
            if item[0] == choice:
                found_pizza = item
                break

        if found_pizza:
            size = input("What size? (small/medium/large)\n> ").lower()
            if size == "small" or size == "medium" or size == "large":
                if size == "small":
                    price = found_pizza[1]
                elif size == "medium":
                    price = found_pizza[2]
                elif size == "large":
                    price = found_pizza[3]

                total += price
                wait_time += MIN_PER_PIZZA
                cart.append(f"{size} {choice}")
                print(f"Added {size} {choice}. Total: ${total}")
            else:
                print("Invalid size. Please try again.")
        else:
            print("That item is not on the menu.")

    if not cart:
        print("Cart is empty. Order cancelled")
        return

    final_total = total + DELIVERY_FEE if order_type == "delivery" else total
    print_header("Order Summary")
    for item in cart:
        print(f"- {item}")
    if order_type == "Delivery":
        print(f"- Delivery Fee: ${DELIVERY_FEE}")
    print(f"\nTotal to pay: ${final_total}")

    # Receipt and confirmation
    while True:
        confirm = input("Would you like to complete your order? (Y/N)\n> ")
        if confirm == "y" or confirm == "yes":
            clear_screen()
            print_header("Receipt")
            print(f"Customer name: {customer_name}\nPhone number: {phone}\nOrder type: {order_type}")
            if order_type == "delivery":
                print(f"Address: {address}")
            print(f"Order: {', '.join(cart)}\nTotal: ${final_total}\nWait time: {wait_time} mins")
            break
        elif confirm == "n" or confirm == "no":
            clear_screen()
            print("Order successfully canceled.")
            break
        else:
            print(ERROR_MESSAGE)


# Menu
while True:
    print_header("Pizza Ordering System")
    reception = input("1) Pick Up\n2) Delivery\n> ").lower()
    if reception == "1" or reception == "pickup" or reception == "pick up":
        print("Pick Up selected")
        pick_up()

    elif reception == "2" or reception == "delivery":
        print("Delivery selected")
        delivery()

    else:
        print(ERROR_MESSAGE)
