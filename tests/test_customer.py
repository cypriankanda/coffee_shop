from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

def test_customer_name_validation():
    c = Customer("ValidName")
    assert c.name == "ValidName"

def test_customer_create_order():
    c = Customer("Alice")
    coffee = Coffee("Mocha")
    order = c.create_order(coffee, 4.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5
