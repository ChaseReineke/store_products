from modules import store
from modules import product


if __name__ == "__main__":
    lincoln = store.Store("lincoln")
    melon = product.Product("melon", 10.00, "fruit")
    switch = product.Product("switch", 200.00, "gaming console")
    snickers = product.Product("snickers", 1.50, "snacks")
    ps4 = product.Product("ps4", 400, "gaming console")
    lincoln.add_product(switch).add_product(melon).add_product(snickers).add_product(ps4)
    for product in lincoln.products:
        print(product.name, product.price, product.category, product.id)
    lincoln.inflation(10)
    melon.update_price(20)
    for product in lincoln.products:
        print(product.name, product.price, product.category, product.id)
    lincoln.sell_product(1)
    for product in lincoln.products:
        print(product.name, product.price, product.category, product.id)
    lincoln.set_clearance("gaming console", 50)
    for product in lincoln.products:
        print(product.name, product.price, product.category, product.id)