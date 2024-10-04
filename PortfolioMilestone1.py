class ItemToPurchase: 
    #init the names so they have values if user does not specify
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description = "EMPTY"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    #print items as listed Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    #calc total so you do not need to do math over and over
    def calc_total_price(self):
        total = self.item_price * self.item_quantity
        return total

# Shopping cart class 
# constructor with name initalized to "none and date "JAnuary 1 2020" 
# list of cart_items 
class ShoppingCart:
    def __init__(self, cust_name = "none", date = "January 1, 2020"):
        self.cust_name = cust_name
        self.date = date
        self.cart_items = []

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)
    
    def remove_item(self, item_name): 
        item_found = False
        for i in self.cart_items: 
            if(i.item_name == item_name): 
                self.cart_items.remove(i)
                item_found = True

        if(item_found == False):
            print('Item not found in cart. Nothing removed.')
    
    def modify_item(self, itemToPurchase, new_price, new_q, new_desc):
        item_found = False
        for i in self.cart_items: 
            if (i.item_name == itemToPurchase.item_name): 
                i.item_price = new_price
                i.item_quantity = new_q
                i.item_description = new_desc
                print(f"Item Modified : {i.item_name}")
                item_found = True
        if(item_found == False):
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        return len(self.cart_items)
    
    def get_cost_cart(self):
        cost_cart = 0
        for i in self.cart_items:
            x = i.item_price * i.item_quantity
            cost_cart += x

        return cost_cart

    def print_total(self):
        print(f"{self.cust_name} - {self.date}")
        print(f"Number of Items : {self.get_num_items_in_cart()}")

        for i in self.cart_items:
            i.print_item_cost()
        print(f"Total : ${self.get_cost_cart()}")

    def print_item_descriptions(self):
        print(f"{self.cust_name} - {self.date}")
        print(f"Item Descriptions")
        for i in self.cart_items:
            print(f"{i.item_name} : {i.item_description}")

def print_menu(shoppingCart):
    menu = """
        MENU
        a - Add item to cart
        r - Remove item from cart
        c - Change item quantity
        i - Output items' descriptions
        o - Output shopping cart
        q - Quit
        Choose an option: """
    
    user_choice = ''
    
    while user_choice != 'q':
        print(menu)
        user_choice = input()
        
        if user_choice == 'a':
            item_name = input("Enter the item name: ")
            item_price = int(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_description = input("Enter the item description: ")
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            shoppingCart.add_item(new_item)
            print(f"{item_name} added to cart.")
        
        elif user_choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shoppingCart.remove_item(item_name)
        
        elif user_choice == 'c':
            item_name = input("Enter the item name to modify: ")
            new_quantity = int(input("Enter the new item quantity: "))
            for i in shoppingCart.cart_items:
                if i.item_name == item_name:
                    i.item_quantity = new_quantity
        
        elif user_choice == 'i':
            shoppingCart.print_item_descriptions()
        
        elif user_choice == 'o':
            shoppingCart.print_total()
        
        elif user_choice == 'q':
            print("Exiting the program.")
        
        else:
            print("Invalid option. Please try again.")

# Milestone 3
cust_name = input("Enter customer's name : ")
current_date = input("Enter todays date : ")
print(f"Customer name: {cust_name}")
print(f"Today's date: {current_date}")

cart = ShoppingCart(cust_name, current_date)
print_menu(cart)