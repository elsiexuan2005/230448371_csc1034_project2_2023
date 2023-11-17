from item import Item
from item_manager import ItemManager
# Examples for item
my_item = Item("Honda", "Car", False, 66, 100.0)
my_item_copy = Item("Honda", "Car", False, 66, 100.0)
other_item1 = Item("Book", "Stationery", True, 10, 6.72)
# Test item.py
print(my_item.get_name())
print(my_item.get_category())
print(my_item.get_perishable())
print(my_item.get_stock())
print(my_item.get_sell_price())
print(str(my_item))
print(repr(my_item))
print("Is it equal to each other?", my_item == my_item_copy)  # Should be true
print("Is it equal to each other?", my_item == other_item1)  # Should be false

# Exceptional case: negative values are not allowed in stock and sell_price
try:
    my_item = Item("Bright", "Category", False, -66, 6.72)
except ValueError as e:
    print(f"ValueError: {e}")
print()
try:
    my_item = Item("Bright", "Category", False, 66, 6.72)
except ValueError as e:
    print(f"ValueError: {e}")

print()
print()
# Test item_manager.py
item_manager = ItemManager([Item("Bread", "Food", True, 10, 10.0)])
print(item_manager.get_items())  # Returns an empty list
print("Add",item_manager.add_item(my_item))  # Test add_item method
print()
# Duplication
copy_item = Item("Bread", "Food", True, 10, 10.0)
print("Is it existed?", item_manager.add_item(copy_item))
print()
# String reperesentation
print(str(item_manager))
print()
print(repr(item_manager))
print()
# Test remove method
print(item_manager.remove_item(my_item))
print("After removing, the list contains:")
print(item_manager.get_items())  #
# Test edit
print(item_manager.add_item(my_item))
other_item1 = Item("Book", "Stationery", True, 10, 6.72)
print(item_manager.edit_item(my_item, other_item1))
print("Current item in the list", item_manager.get_items())
print()
# Test search method
print(item_manager.search_by_category("Food"))  # Category
print(item_manager.search_by_perishable(True))  # Perishable
print(item_manager.search_by_sell_price(10.0))  # Sell price
# Test apply discount
print("Before applying discount", item_manager.get_items())
print(item_manager.apply_discount_to_items("Book",10))
print("After applying discount",item_manager.get_items())
print()
# Purchase method
print(item_manager.get_items())
purchase_item1=["Bread","Book"]
print("No membership?",item_manager.purchase_available_items(purchase_item1,False))  # If is_member is False, no discount
print("Have membership but pay less 50p?",item_manager.purchase_available_items(purchase_item1,True))  # Apply discount for 5 percents
print(item_manager.add_item(my_item))
print(item_manager.get_items())
purchase_item2 =["Bread","Book","Honda"]
print("Have membership and pay more 50p?", item_manager.purchase_available_items(purchase_item2,True))  # Apply discount for 10 percents
print()
print()
# Load data from csv file
print(item_manager.load_from_file("sample_data.csv"))
print()
# Save data to a new file
print(item_manager.save_to_file("new_data.csv"))



