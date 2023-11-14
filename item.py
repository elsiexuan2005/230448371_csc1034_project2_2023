class Item:

    def __init__(self, name, category, perishable, stock, sell_price):
        self.__name = name
        self.__category = category
        self.__perishable = perishable
        self.__stock = stock
        if self.__stock <= 0:
            raise ValueError("Stock should be in positive value")
        self.__sell_price = sell_price
        if self.__sell_price <= 0:
            raise ValueError("Sell price should be in positive value")


    def get_name(self):
        if not isinstance(self.__name, str):
            raise TypeError("Name should be in string")
        else:
            return self.__name

    def get_category(self):
        if not isinstance(self.__category, str):
            raise TypeError("Category should be in string")
        else:
            return self.__category

    def get_perishable(self):
        if not isinstance(self.__perishable, bool):
            raise TypeError("Perishable should be in boolean type")
        else:
            return self.__perishable

    def get_stock(self):
        if not isinstance (self.__stock, int):
            raise ValueError("Stock should be in integer")
        else:
            return self.__stock


    def get_sell_price(self):
        if not isinstance(self.__sell_price, float):
            raise ValueError("Sell price should be in float")
        else:
            return self.__sell_price

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

