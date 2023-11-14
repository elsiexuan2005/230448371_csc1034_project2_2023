class Item:

    def __init__(self, name, category, perishable, stock, sell_price):
        self.__name = name
        self.__category = category
        self.__perishable = perishable
        self.__stock = stock
        self.__sell_price = sell_price

    def get_name(self):
        if not isinstance(self.__name, str):
            raise TypeError("Name should be in string")

    def get_category(self):
        if not isinstance(self.__category, str):
            raise TypeError("Category should be in string")

    def get_perishable(self):
        if not isinstance(self.__perishable, bool):
            raise TypeError("Perishable should be in boolean type")

    def get_stock(self):
        if isinstance (self.__stock, int) and self.__stock >= 0:
            raise TypeError("Stock should be in integer")


    def get_sell_price(self):
        if not isinstance(self.__sell_price, float) and self.__sell_price < 0:
            raise TypeError("Sell price should be in float and non-negative")

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __hash__(self):
        pass

