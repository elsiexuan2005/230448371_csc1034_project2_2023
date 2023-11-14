from item import Item

my_item = Item("Bright", "Category", False, 66, 6.72)

# Test item.py
print(my_item.get_name())
print(my_item.get_category())
print(my_item.get_perishable())
print(my_item.get_stock())
print(my_item.get_sell_price())
print(str(my_item))
print(repr(my_item))

# Exceptional case: negative values are not allowed in stock
try:
    my_item = Item("Bright", "Category", False, -66, 6.72)
except ValueError as e:
    print(f"ValueError: {e}")



