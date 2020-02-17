import requests, os, json, base64, hashlib, hmac
from requests.exceptions import HTTPError
from item import Item

"""
Module uses the UPC Database to query for items. Information 
can be found here: 
https://upcdatabase.org/
https://upcdatabase.org/api-search-get
"""
# Item ID to test with called: Twist-Erase III Mechanical Pencil, (0.9mm), Black Barrel
test_item_id = "072512099681"


def _set_secret(search_term, secrets_file='secrets.json'):
    """
    Gets a key from a secrets JSON file. 
    File needs to be located in same directory.
    {
        "key" : "[YOUR-KEY]"
    }
    :args:
        secrets_file: Optional path to secrets file
        search_term = A string to search the JSON file for
    Returns:
        Returns the secret found in the JSON file.
        If key is not present or fails returns -1
    """
    with open(secrets_file, encoding='utf-8') as secrets_file:
        secrets = json.load(secrets_file)
    try:
        return secrets[search_term]
    except:
        return "Invalid secrets search term, please check the secrets file." 


def _calc_signature(upc_code):
    """
    Calculates the hash value according to the digit-eyes API
    :args:
        upc_code: Needs UPC you are searching with
        secrets_file: Option argument for the secrets file
    """
    # Have to encode the auth_key and upc-code in UTF-8 before hasing
    auth_key = str(_set_secret('auth_key')).encode('utf-8')
    sha_hash = hmac.new(auth_key, str(upc_code).encode('utf-8'), hashlib.sha1)
    return base64.b64encode(sha_hash.digest()).decode("utf-8") #Need to decode or else there will be a leading b' to reprsent bytes


def _create_item_object(item):
    """
    Creates an Item object out of the given request data
    Returns: An Item object type. 
    args: Requires a dict/JSON type request string
    """
    if item['alias'] is not '': 
        pass
    if item['msrp'] is not '':
        pass
    if item['category'] is not '': 
        pass

    #item_obj = Item(name=item['name'])

    #for i in item_json:
     #   print("{item} : {value}".format(item=i, value=item_json[i]))


def query_for_item(item):
    """
    Queries the DB for the item
    :args:Takes a UPC code to search for
    :returns: An item object w/ basic information
    """
    base_query_url = "http://digit-eyes.com/gtin/v2_0/?"
    app_key = _set_secret('app_key')
    signature = _calc_signature(item)
    query_string = base_query_url + "upcCode=" + item  + "&app_key=" + app_key + "&signature=" + signature + "&language=en"

    try:
        response = requests.get(query_string)
        response.raise_for_status()
    except HTTPError as http_err: 
        return "There was an error with your request ", http_err
    except Exception as e: 
        return "There was an error with the request ", e
    else:
        #return _create_item_object(response.json())
        return response.json()
        # Pass to another function to clean response or pass as response object? 

print(query_for_item(test_item_id))