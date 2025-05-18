from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_order_initialization_and_properties():
    customer = Customer("Test")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 5.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.5
