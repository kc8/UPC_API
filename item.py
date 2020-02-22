"""
Class of the item searched for or retrived from the database. 
This could be a scanned barcoded item or from antoher source
"""

class Item:

    def __init__(self, name, 
                upc=None, 
                price=None, 
                alias='_blank_',
                category='unknown', 
                size=None):
        """
        Creates an item object with some varius information. 
        :args:
            name: Name of the item
            upc: UPC of item for additional lookups default is None. 
            price: Optional Price of the item, if known otherwise $0
            alias: Optional alias for the item otherwise _blank_ is used.
            category: Categorize the item (Produce, Office Supplies, etc.)
        """ 

        self.name = name
        self.alias = alias
        self.price = price
        self.category = category
        self.size = size
        self.tax = None
    

    def __iter__(self):
        """
        Not yet implemented
        """
        pass


    def __next__(self): 
        pass


    def __eq__(self, comp_item): 
        """
        Not yet implemented.
        """
        pass


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
    
    
    def calculate_tax(self, tax_percent):
        """
        Returns calculated tax and stores its. Price must be set first
        :args: Tax percent in decimal form
        :return: Tax + price or error
        """
        if self.price is not None:
            try:
                self.tax = (self.price * tax_percent) + self.price
                return self.tax
            except Exception as e:
                return e 
        else: 
            return "Price not set"