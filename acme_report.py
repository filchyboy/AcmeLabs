'''

'''
import random
from random import randint
from acme import Product

num_products = 30


def generate_products(num_products):
    '''
    Generates a random list of products for the ACME corp based on some
    constraints passed to us by the clueless overlords of the corporation.
    '''
    for _ in range(num_products):
        name_joined = random.choice(fname) + " " + random.choice(lname)
        name_list.append(name_joined)
        price_list.append(randint(5, 100))
        weight_list.append(randint(5, 100))
        flam_list.append(random.uniform(0, 2.5))


def inventory_report(num_products):
    '''
    Most of this code is not needed currently. Only unique_names is currently
    used. But there is always the future of ACME Corp in the remaining code.
    '''
    for _ in range(num_products):
        prod_list.append(name_list[_])
        unique_names.append(name_list[_])
        prod_list.append(price_list[_])
        prod_list.append(weight_list[_])
        prod_list.append(flam_list[_])


def export_inventory(name_list):
    for _ in range(num_products):
        print("Product Name:", name_list[_])

# Marketing department approved drivel
fname = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
lname = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

# A bunch of empty sets to be filled, like my heart.
name_list = []
price_list = []
weight_list = []
flam_list = []
prod_list = []
unique_names = []
average_weight = []
average_price = []
average_flammability = []

# Call the function declared above.
generate_products(num_products)
inventory_report(num_products)

# Isolate the unique names of products
set_list = set(name_list)

# Print out THE OFFICIAL REPORT OF IMPORTANT THINGS

print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
export_inventory(name_list)
print("Unique Product Names", len(set_list))
print("Average Weight", sum(weight_list)/len(weight_list))
print("Average Price", sum(price_list)/len(price_list))
print("Average Flammability", sum(flam_list)/len(flam_list))
