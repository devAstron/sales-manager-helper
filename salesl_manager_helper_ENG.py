# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:04:13 2023

@author: Bahodir
"""
 # 1. The purpose of creating the function is to get information from the seller and
 # save to list and return this list
# 2. We create a function that takes the product from the buyer to its seller
# Checks if there is and gives it out with prices
def for_sales_manager():
    '''The function of receiving information from the seller and returning it'''
    products = { }
    print("Hello, we will now get information about the products: ")
    
    while True:
        product = input(f'Enter the name of the product: ')
        products[product] = input(f'Enter the price of {product.title()}: ').lower()
        request = input("Do you want to add more products? (Yes - 1, No - 0): ")
        if request == '0':
            break
        
    print("Accepted! The listed products are as follows: ")
    for product, price in products.items():
        print(f"{product.title()}: {price}")
    return products

def for_client():
    needed_products = []
    
    print("We will now create a list of products you need: ")
    while True:
        product = input(f"Enter the product: ").lower()
        needed_products.append(product)
        request = input("Do you need more products? (Yes - 1, No - 0): ")
        if request == '0':
            break
        
    print("Accepted!")
    return needed_products

sales_products = for_sales_manager()   
needed_products = for_client()
for product in sales_products:
    if product in needed_products:
        print(f"{product.title()} is available in the store and costs {sales_products[product]}.")

    
    
    
    
    
    
    



        