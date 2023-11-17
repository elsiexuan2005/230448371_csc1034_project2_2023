from item import Item
from item_manager import ItemManager

# Examples for item
my_item = Item("Bright", "Category", False, 66, 6.72)
my_item_copy = Item("Bright", "Category", False, 66, 6.72)
other_item = Item("Bright", "Category", False, 10, 6.72)

# Test item.py
print(my_item.get_name())
print(my_item.get_category())
print(my_item.get_perishable())
print(my_item.get_stock())
print(my_item.get_sell_price())
print(str(my_item))
print(repr(my_item))
print("Is it equal to each other?", my_item == my_item_copy)  # Should be true
print("Is it equal to each other?", my_item == other_item)  # Should be false

# Exceptional case: negative values are not allowed in stock
try:
    my_item = Item("Bright", "Category", False, -66, 6.72)
except ValueError as e:
    print(f"ValueError: {e}")
print()
print()
# Test item_manager.py
item_manager = ItemManager()
print(item_manager.get_items())  # Returns an empty list
print(item_manager.add_item(my_item))  # Test add_item method
print()
# Duplication
print("Is it existed?", item_manager.add_item(my_item_copy))
print()
print(str(item_manager))
print()
print(repr(item_manager))
print()
# Test remove method
print(item_manager.remove_item(my_item))
print(item_manager.get_items())  # Should return empty list
# Test edit
print(item_manager.add_item(my_item))
print(item_manager.edit_item(my_item, other_item))
print("Current item in the list", item_manager.get_items())
print()
# Test search method
print(item_manager.search_by_category("Category"))  # Category
print(item_manager.search_by_perishable(True))  # Perishable, return None
print(item_manager.search_by_sell_price(6.72))  # Sell price
# Test apply discount
print("Before applying discount", item_manager.get_items())
print(item_manager.apply_discount_to_items("Bright",10))
print("After applying discount",item_manager.get_items())