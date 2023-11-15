class ItemManager:

    def __init__(self, items=None):
        if items is None:
            self.__items = []
        else:
            self.__items = items

    def get_items(self):
        return self.__items

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def edit_item(self, old_item, new_item):
        pass

    def search_by_category(self, category):
        pass

    def search_by_perishable(self, perishable):
        pass

    def search_by_sell_price(self, sell_price):
        pass

    def apply_discount_to_items(self, names, discount):
        pass

    def purchase_available_items(self, names, is_member):
        pass

    def load_from_file(self, file_name):
        pass

    def save_to_file(self, file_name):
        pass
