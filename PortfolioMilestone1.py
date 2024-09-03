class ItemToPurchase: 
    #init the names so they have values if user does not specify
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    #print items as listed Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    #calc total so you do not need to do math over and over
    def calc_total_price(self):
        total = self.item_price * self.item_quantity
        return total

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
