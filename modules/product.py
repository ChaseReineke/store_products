class Product:
    id_counter = 1
    def __init__(self, name, price, category):
        self.name = name
        self.price = round(price,2)
        self.category = category
        self.id = Product.id_counter
        Product.id_counter += 1

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
        return self

    def update_price(self, percent_change, is_increased = True):
        if is_increased == True:
            self.price = round(self.price * (1+percent_change/100), 2)
        else:
            self.price = round(self.price*(1-percent_change/100), 2)
        return self

if __name__ == "__main__":
    melon = Product("melon", 10, "fruit")
    melon.print_info()
    melon.update_price(25)
    melon.print_info()
    melon.update_price(25, False)
    melon.print_info()