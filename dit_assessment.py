"""This is a pizza ordering system that allows customers to place pick up or delivery orders."""

# Variables
ERROR_MESSAGE = "An error has occurred. Please enter a valid input"
DELIVERY_FEE = 10
MIN_PER_PIZZA = 15

# List of pizza options:(Name, Small, Medium, Large)
pizza = [
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
    name = input("Name for Pick Up\n> ")
    phone_number = get_num("Phone number\n> ")
    order(name, "pick up", phone_number)


def delivery():
    """Gather customer details for a delivery order and start the ordering process."""
    name = input("Name for Delivery\n> ")
    address = input("Address for Delivery\n> ")
    phone_number = get_num("Phone number\n> ")
    order(name, "delivery", phone_number, address)


def order(customer_name, order_type, phone, address="N/A"):
    """Manage the main pizza ordering loop, cart management, and receipt generation."""
    # Variables for order (not at top so they reset for each order)
    cart = []
    total = 0
    wait_time = 0

    while True:
        for item in pizza:
            print(f"{item[0]} | Small: ${item[1]} | Medium: ${item[2]} | Large: ${item[3]}")
        choice = input("Enter pizza name (or type 'done' to finish)\n> ").lower().strip()
        if choice == "done":
            break

        found_pizza = None
        for item in pizza:
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

    print(f"Your total is ${total + DELIVERY_FEE if order_type == 'delivery' else total}")

    # Receipt and confirmation
    while True:

        confirm = input("Would you like to complete your order? (Y/N)\n> ")
        if confirm == "y" or confirm == "yes":
            print(f"Final receipt:\nName: {customer_name}\nType: {order_type}")

            if order_type == "delivery":
                print(f"Address: {address}")

            print(f"Order: {', '.join(cart)}\nTotal: ${total + DELIVERY_FEE if order_type == 'delivery' else total}\nWait time: {wait_time} mins")
            break

        elif confirm == "n" or confirm == "no":
            print("Order successfully canceled.")
            break

        else:
            print(ERROR_MESSAGE)


# Menu
while True:
    reception = input("1) Pick Up\n2) Delivery\n> ").lower()
    if reception == "1" or reception == "pickup" or reception == "pick up":
        print("Pick Up selected")
        pick_up()

    elif reception == "2" or reception == "delivery":
        print("Delivery selected")
        delivery()

    else:
        print(ERROR_MESSAGE)

# keep new line at end of file
"""
to add:
record testing video (remember to test negative cases) (talk during the video)
add .strip() to phone number input (not nessasary)
make the user interface look nicer and .sleep's
redo varible names
add ablity to remove items from cart
change file and / repo name
change project discription
change key spesifications
"""