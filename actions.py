# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.YourGoToStore.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print("- %" % store.name)




def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
        else:
            return False
        
 

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    store_found = False
    while not store_found:
        print_stores()
        store_name = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
        if store_name.lower() == "checkout":
            return checkout
        picked_store = get_store(store_name)
        if picked_store:
            break
            print("No store with that name. Please try again.")

    return picked_store


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    print ("Type the products that you'd like to add to your cart. Make sure they are spelled exatly as shown.")
    print("Type \"back\" to go back to the main menu where you can checkout.")
    user_input = ""
    while user_input.lower() != "back":
        for product in picked_store.products:
            if user_input.lower() == product.name.lower():
                cart.add_to_cart(product)
        user_input = input()

    return user_input

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    user_input = ""
    while user_input.lower() != "checkout":
        user_input = ""
        picked_store = pick_store()
        if picked_store == "checkout":
            break

        picked_store.print_products()
        user_input = pick_products(cart, picked_store)

    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
