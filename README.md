# Python Wrapper for UPC Lookup Using Digit Eyes API

A module that will query the Digit Eyes API and return an Item object. I am currently working to improve this package with more features and error checking.

You will need an app key and auth key from digit-keys. You can sign up here: http://www.digit-eyes.com/

## Current State
You can query the API database with a UPC code and receive an item object back that will hold the name of the item with a few other data points. See 'item' docuemntation below

**Why Return an item object**

The idea is to use the item object to store in your own database or used in another application. I also wanted to abstract the API away from the nmodules as much as possible incase I want to change API providers in the future. 


## Item
An item has the following properties. All optional except for 'name'
* Name
* Alias (if the name is to long)
* Price
* Category (If you want to cateogrize items)
* Size (used for lb/ or general servicing size)
* Tax (needs to be calculated first)

An item has teh following functions: 
* Set and update functions for the properties (if needed)
* Calculate tax. Takes a tax percent as float in decimal (i.e. 20% 0.20)


## Query
A query only gets and sets the name of an item. Working on seeing if there is 
any other useful information to set in item. 
Also looking for another API that returns price.


Example:
```python
from upc_query.upc_lookup import BarcodeQuery
from upc_query.item import Item

query = BarcodeQuery(file_location="[FULL-PATH-TO-KEY-FILE]/secrets.json", setup_keys_with_file=True)
# can also pass BarcodeQuery your app and authkey with (app_key=[string_here], auth_key= [string_here],)

milk_search = query.lookup('093966000337') #  item object
print(milk_search)
print(type(milk_search))
```
Output:
```python
Organic Valley Half & Half
<class 'upc_query.item.Item'>
```

## More updates to come! 

I will be using this module for a larger shopping list project with a barcode scanner and Raspberry Pi. 