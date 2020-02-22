import requests, os, json, base64, hashlib, hmac, logging
from requests.exceptions import HTTPError
from item import Item

"""
Module uses the UPC Database to query for items. Information 
API: http://www.digit-eyes.com/
You can make an account on their site and get your keys, adding them to 
a secrets.json file. 
You have ~500 free requests on their site
"""
# Item ID to test with called: Twist-Erase III Mechanical Pencil, (0.9mm), Black Barrel
test_item_pen = "072512099681"
test_item_milk = "093966000337" # Nature Valley half & half
test_invalid_search = "0939660003370"


# To-Do
#    Need to ensure that the file option will get the working directory of the user. 
class BarcodeQuery:

    def __init__(self, app_key=None,
                auth_key=None,
                setup_keys_with_file=False,
                file_location="./"
                ):
        self.auth_key = auth_key
        self.app_key = app_key
        self.use_secrets_file = setup_keys_with_file
        self.secrets_file = file_location

        if setup_keys_with_file == True:
            self.app_key = self._set_secret_with_file('app_key')
            self.auth_key = self._set_secret_with_file('auth_key')


    def _config_logging_for_barcode(self, status=True, level='warning'):
        """
        Configures logigng. Defaul is on and set to warning level. Places log in current file. Can be overriden or change if need.
        """
        if status == True:
            logging.basicConfig(filename='./UPC_Logs/product_API.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.debug('Logging is on')
        else:
            return "Logging for product API is off"


    def _set_secret_with_file(self, search_term):
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
        with open(self.secrets_file, encoding='utf-8') as secrets_file:
            secrets = json.load(secrets_file)
        try:
            return secrets[search_term]
        except:
            return "Using files options to setup keys failed, please check secrets file" 

    # To-Do. Create custom exceptions/errors for calculating the signature
    def _calc_signature(self, upc_code):
        """
        Calculates the hash value according to the digit-eyes API
        :args:
            upc_code: Needs UPC you are searching with
            secrets_file: Option argument for the secrets file
        """
        # Have to encode the auth_key and upc-code in UTF-8 before hasing
        if self.app_key and self.auth_key:
            auth_key = str(self.auth_key).encode('utf-8')       
        else:  # Try with the file
            auth_key = str(self._set_secret_with_file('auth_key')).encode('utf-8') 
        sha_hash = hmac.new(auth_key, str(upc_code).encode('utf-8'), hashlib.sha1)
        return base64.b64encode(sha_hash.digest()).decode("utf-8") # Decode or there will be a leading b' representing bytes


    def _create_item_object(self, item):
        """
        Creates an Item object out of the given request data
        Due to API limitations only creates an object with name and UPC
        :args: Requires a dict/JSON type request string. 
        :return: Item object. 
        """

        if item['description'] == '': 
            return "Item does not have a valid description"
        else:
            product = Item(name=item['description'], upc=item['upc_code'])
        
        return product

    # TO-D0. Check if valid UPC before we query the API
    def lookup(self, item):
        """
        Queries the DB for the item using Digit Eyes API
        This returns an item object. 
        :args: UPC code to search for. 
        :returns: An item object w/ basic information
        """
        base_query_url = "http://digit-eyes.com/gtin/v2_0/?"
        app_key = self.app_key
        signature = self._calc_signature(item)
        query_string = base_query_url + "upcCode=" + item  + "&app_key=" + app_key + "&signature=" + signature + "&language=en"

        try:
            response = requests.get(query_string)
            response.raise_for_status()
        except HTTPError as http_err: 
            logging.error("There was an error with the query: {err}".format(err=http_err))
            return Item("Invalid Item")
        except Exception as e: 
            logging.error("There was an exception processing the API: {err}".format(err=e))
            return Item("Invalid Item")
        else:
            return self._create_item_object(response.json())

query  = BarcodeQuery(setup_keys_with_file=True, file_location='./secrets.json')