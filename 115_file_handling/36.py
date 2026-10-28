from ecommerce.products.catalog import products
from ecommerce.customers.records import customers
from ecommerce.orders.records import orders
from ecommerce.payments.methods import payment_methods

print("Products:", products())
print("Customers:", customers())
print("Orders:", orders())
print("Payment methods:", payment_methods())
