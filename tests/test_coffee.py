from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_coffee_name_validation():
    c = Coffee("Espresso")
    assert c.name == "Espresso"

def test_coffee_orders_and_customers():
    c1 = Customer("Bob")
    c2 = Customer("Jim")
    coffee = Coffee("Latte")
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 4.0)
    assert len(coffee.orders()) == 2
    assert len(coffee.customers()) == 2
