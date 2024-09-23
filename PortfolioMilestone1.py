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
'''
#part 1 print the item that is created using the class and method
item1 = ItemToPurchase("banana", 5, 6)
item1.print_item_cost()

#part 2 user has input, take in the name price and quant, store in var
print("Item 1")
item_1_name = input("Enter the item name : ")
item_1_price = int(input("Enter the item price : "))
item_1_quant = int(input("Enter the item quantity : "))

print("Item 2")
item_2_name = input("Enter the item name : ")
item_2_price = int(input("Enter the item price : "))
item_2_quant = int(input("Enter the item quantity : "))

#put those temps into the objects of the class
item1 = ItemToPurchase(item_1_name, item_1_price, item_1_quant)
item2 = ItemToPurchase(item_2_name, item_2_price, item_2_quant)

#calc the total
total_cost = item1.calc_total_price() + item2.calc_total_price()

print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total : ${total_cost}")

# MILESTONE 2 
cart = ShoppingCart("Sean James", "Sept 2024")
item1.item_description = input("Give description for item 1 : ")
item2.item_description = input("Give description for item 2 : ")
item_to_remove = input("Enter item name to remove : ")
cart.add_item(ItemToPurchase("cup"))
item_to_edit = input("Enter item name to edit : ")
item_mod = ItemToPurchase(item_to_edit)
new_q = int(input("Enter new quantity  :"))
new_p = int(input("Enter new price :"))
new_d = input("Enter new description  :")
cart.add_item(item1)
cart.add_item(item2)
cart.remove_item(item_to_remove)
cart.modify_item(item_mod,new_p, new_q, new_d)

cart.print_total()
cart.print_item_descriptions()
'''

# Milestone 3
cart = ShoppingCart("Sean James", "Sept 2024")
print_menu(cart)