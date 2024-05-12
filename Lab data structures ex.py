#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Step 1
products_list = ["t-shirt", "mug", "hat", "book", "keychain"]

# Step 2
inventory = dict()

# Step 3
for i in range(len(products_list)):
    print("Amount of:", products_list[i])
    valor = input()
    inventory[products_list[i]] = int(valor)
    print()

# Step 4
custom_orders = set()

# Step 5
amount = 0
while amount < 3:
    print("Name of product", amount)
    product = input()

    if products_list.count(product) > 0:
        custom_orders.add(product)
        amount += 1
        print()
        print("Product added to cart")
        print()
    else:
        print()
        print("No availability of product", product)
        print("Choose another product")
        print()

# Step 6
print("Customer orders: ", custom_orders)

# Step 7
order_status = dict()

def total_products():
    return len(custom_orders)

def percentage_orders():
    return (len(custom_orders)/len(products_list)) * 100

order_status["percentage_products"] = percentage_orders()
order_status["total_order"] = total_products()

# Step 8
print("Order statistics:")
print("Total Products Ordered: ", order_status.get("total_order"))
print("Percentage of Products Ordered: ", order_status.get("percentage_products"))

# Step 9
for product in custom_orders:
    inventory[product] = inventory.get(product)-1

# Step 10
print(inventory)
          



