from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

# Sample data
alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 3.5)
alice.create_order(latte, 4.5)
bob.create_order(latte, 5.0)
bob.create_order(espresso, 2.5)

print("Most aficionado for latte:", Customer.most_aficionado(latte).name)
print("Latte average price:", latte.average_price())
