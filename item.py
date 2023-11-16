class Item:

    def __init__(self, name, category, perishable, stock, sell_price):
        self.__name = name
        self.__category = category
        self.__perishable = perishable
        self.__stock = stock
        if self.__stock < 0:
            raise ValueError("Stock should be in positive value")
        self.__sell_price = sell_price
        if self.__sell_price < 0:
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
        if not isinstance(self.__stock, int):
            raise ValueError("Stock should be in integer")
        else:
            return self.__stock

    def get_sell_price(self):
        if not isinstance(self.__sell_price, float):
            raise ValueError("Sell price should be in float")
        else:
            return self.__sell_price

    def __str__(self):
        return f" \nName:{self.__name} \nCategory: {self.__category} \nPerishable: {self.__perishable} \nStock: {self.__stock} \nSelling price: {self.__sell_price}"

    def __repr__(self):
        return f"Item({self.__name},{self.__category},{self.__perishable},{self.__stock},{self.__sell_price})"

    def __hash__(self):
        return hash((self.__name, self.__category, self.__perishable, self.__stock, self.__sell_price))

    def __eq__(self, other):
        print("Performing equality check")
        if isinstance(other, Item):
            return self.__name == other.__name and self.__category == other.__category and self.__perishable == other.__perishable and self.__stock == other.__stock and self.__sell_price == other.__sell_price
        else:
            return False
