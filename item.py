"""
Creates an object of the item.
"""

class Item:

    def __init__(self, name, 
                price=00.00, 
                alias='_blank_',
                category='unknown'):
        """
        Creates an item object.
        :args:
            name: Name of the item
            price: Optional Price of the item, if known otherwise $0
            alias: Optional alias for the item otherwise _blank_ is used.
            category: Categorize the item (Produce, Office Supplies, etc.)
        """ 

        self.name = name
        self.alias = alias
        self.price = price
        self.category = category
    
    def set_price(self, price): 
        """
        Updates or sets the price of the item
        :args:
            price: Known price for the item.
        """
        self.price = price
    
    def updapte_alias(self, new_alias):
        """
        Update the alias or nick-name for the item
        :args:
            new_alias: The new alias to replace the old.
        """
        self.alias = new_alias
    

    def update_category(self, new_category):
        """
        Update the category for the item
        :args:
            new_category: Change the category of the item.
        """
        self.category = new_category 