import csv
class ItemManager:
    def __init__(self, items=None):
        if items is None:
            self.__items = []
        else:
            self.__items = items

    def get_items(self):
        return self.__items

    def __str__(self):
        return f"Detail of the items: \n{self.__items}"

    def __repr__(self):
        return f"Item({self.__items})"

    def add_item(self, item):
        if self.__items is None:
            self.__items.append(item)
        else:
            if any(item == i for i in self.__items):
                return f"This item is already existed"
            else:
                self.__items.append(item)
                return f" {item} is added"

    def remove_item(self, item):
        if self.__items is not None:
            if any(item == i for i in self.__items):
                self.__items.remove(item)
                return "The {item} is removed"
            else:
                return f"{item} is not in the list"

    def edit_item(self, old_item, new_item):
        edit = False
        for i, item in enumerate(self.__items):
            if item == old_item:
                self.__items[i] = new_item
                edit = True
        return edit

    def search_by_category(self, category):
        for item in self.__items:
            if item.get_category() == category:
                return item

    def search_by_perishable(self, perishable):
        for item in self.__items:
            if item.get_perishable() == perishable:
                return item

    def search_by_sell_price(self, sell_price):
        for item in self.__items:
            if item.get_sell_price() == sell_price:
                return item

    def apply_discount_to_items(self, names, discount):
        for item in self.__items:
            if item.get_name() in names:
                item.set_selling_price(item.get_sell_price() * (1 - (discount / 100)))

    def purchase_available_items(self, names, is_member):
        cost = 0.0
        for purchase_item in self.__items:
            if purchase_item.get_name() in names:
                cost += purchase_item.get_sell_price()
                purchase_item.set_stock(purchase_item.get_stock() - 1)
        if is_member is False:
            return cost
        else:
            if cost >= 50.0:
                return cost - (cost * 0.1)
            else:
                return cost - (cost * 0.05)

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                print(row)
                self.__items.append(row)

    def save_to_file(self, file_name):
        pass
