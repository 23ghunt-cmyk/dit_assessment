# Variables
error_message = "An error has occurred. Please enter a valid input"
wait_time = 0
total = 0
delivery_check = False

# Functions
def get_num(prompt):
    """other thing"""
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print(error_message)

def pick_up():
    """thing"""
    customer_name = input("Name for Pick Up\n> ").lower()
    customer_phone_number = get_num("Phone number\n> ")
    order()

def delivery():
     """not thing"""
     delivery = True
     customer_name = input("Name for Pick Up\n> ").lower()
     customer_address = input("Address for Dilivery\n> ").lower()
     customer_phone_number = get_num("Phone number\n> ")
     order()

def order():
     """ok"""
     while True:
          # add list of items
          cart = input("Type 'Done' to finish ordering\nEnter order\n> ").lower()
          if cart == "done":
               break
          else:
               wait_time =+ 5
               # add price
     purchice = input(f"Your total is {total}\nWould you like to complete your order (Y/N)\n> ").lower() # fix spelling and print list of ordered items and their price
     if purchice == "y" or purchice == "yes":
          print(f"Name: {}")
          # add purchiceing message including total cost and customer info and order type (deliver or pick up)
     elif purchice == "n" or purchice == "no":
          print("Order sucsessfully canceled") # check spelling
     else:
          [print(error_message)]



# List of pizza options
pizza = [
    {"name": "alphabet soup pizza","small": 10,"medium": 20,"large": 30},
    {"name": "hawian pizza","small": 10,"medium": 20,"large": 30},
    {"name": "meat lovers pizza","small": 10,"medium": 20,"large": 30},
    {"name": "margherita pizza","small": 10,"medium": 20,"large": 30},
    {"name": "pepperoni pizza","small": 10,"medium": 20,"large": 30},
    {"name": "gravel pizza","small": 10,"medium": 20,"large": 30},
    {"nam3e": "baked bean pizza","small": 10,"medium": 20,"large": 30},
    {"name": "sushi","small": 10,"medium": 20,"large": 30},
    {"name": "mayonnaise","small": 10,"medium n": 20,"large m": 30},
    {"name": "escalator","small": 10,"medium n": 20,"large m": 30},
    {"name": "chair","small": 10,"medium n": 20,"large m": 30},
    {"name": "wood chunk","small": 10,"medium n": 20,"large m": 30},
]

# Menu
while True:
        reception = input("1) Pick Up\n2) Delivery\n> ").lower()
        if reception == "1" or reception == "pickup" or reception == "pick up":
            print("Pick Up selcected")
            pick_up()

        elif reception == "2" or reception == "delivery":
            print("Delivery selected")
            delivery()

        else:
             print(error_message)


"""
to add:
finish ordering system
add comments to all functions
make the list viewable
rework wait time
add another function with a return value or other
"""