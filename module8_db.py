class Pizza:
    def __init__(self, toppings, sauce):
        # Validating inputs
        if not isinstance(toppings, str) or not isinstance(sauce, str):
            raise ValueError("Toppings and sauce must be strings!")
        
        self.toppings = toppings
        self.sauce = sauce
        self.__secret_ing = "red pepper"  # private attribute

    def make_pizza(self):
        print(f"Combined dough, {self.toppings}, {self.sauce}, and a secret ingredient!")

    # Method to access the private attribute
    def get_secret_ingredient(self):
        return self.__secret_ing

    # Optional: A setter method to allow modifying the private attribute safely
    def set_secret_ingredient(self, new_ingredient):
        if not isinstance(new_ingredient, str):
            raise ValueError("Secret ingredient must be a string!")
        self.__secret_ing = new_ingredient

# Create an instance of Pizza class
yummy_pizza = Pizza("pineapple and bacon", "marinara")
yummy_pizza.make_pizza()

# Accessing the secret ingredient via the getter method
print(f"Secret ingredient is: {yummy_pizza.get_secret_ingredient()}")

# Optionally modify the secret ingredient
yummy_pizza.set_secret_ingredient("garlic powder")
yummy_pizza.make_pizza()