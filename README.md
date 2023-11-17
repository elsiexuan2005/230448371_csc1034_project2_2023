# 230448371_csc1034_project2_2023
Description of the project:
This project is designed to manage items and perform various operations on them. It is a good practise of Python

# Functionalities
Item.py
----------
 + a constructor of item class with such instance attributes: name, category, perishable, stock and price

 + a variety of getter and setter method 

+ a string representation to make the representation more clear

+ a hash method to hash the item object 

+ a checking equality method to check the equality between 2 item objects

Item manager.py
--------------
+ a constructor of item manager class that take item object as a list

+ a get item method that returns the list of Item objects stored in the ItemManager.

+ a string representation method to represent the strings from item manager 

+ add, remove, edit Item methods: Allows adding, removing, and editing Item objects within the item manager

+ search method retrieves a list of Item objects

+ apply discount method applies a discount to specified item objects.

+ purchase available item methods updates the stock and calculates the total cost for purchased items.

+ load from and save to file method read from and write to a CSV file containing item details.

csv file
----------
+ contain data details
