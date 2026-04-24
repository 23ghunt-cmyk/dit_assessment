# Variables
error_message = "An error has occurred. Please try again"
wait_time = 0

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
     delivery = "delivered"
     customer_address = input("Address for Dilivery\n> ").lower()
     customer_phone_number = get_num("Phone number\n> ")
     order()

def order():
     """ok"""
     print(pizza)
     while True:
          cart = input("Type 'Done' to finish ordering\nEnter order\n> ").lower()
          if cart == "done":
               break
          else:
               wait_time =+ 5



# List of pizza options
pizza = [
    {"name": "alphabet soup pizza","small": 10,"medium": 20,"large": 30},
    {"name": "hawian pizza","small": 10,"medium": 20,"large": 30},
    {"name": "meat lovers pizza","small": 10,"medium": 20,"large": 30},
    {"name": "margherita pizza","small": 10,"medium": 20,"large": 30},
    {"name": "pepperoni pizza","small": 10,"medium": 20,"large": 30},
    {"name": "gravel pizza","small": 10,"medium": 20,"large": 30},
    {"name": "baked bean pizza","small": 10,"medium": 20,"large": 30},
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