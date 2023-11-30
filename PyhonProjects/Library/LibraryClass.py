import json
import functools

class DataItem():
    """A class to define all attributes of a data item"""
    # Defining the structure of the data item.
    # This can be changed and there is a function that will update the old data to the updated format.
    item_info = ["type", "details", "location", "value", "restrictions"]
    details_list = {
                "book": ["title", "author", "genre", "language", "publication year"],
                "customer": [],
                "employee": [],
                "library": ["address", "book total",	"popular", "employees"]
                }
    restrictions = {
                "book": [],
                "customer": [],
                "employee": [],
                "library": []
                }
    file_name = "ItemData.json"
    serial_length = 6
    
    def __init__(self):
        pass
    
    @staticmethod
    def item_format():
        return DataItem.details_list.keys()
    
    @staticmethod
    @functools.cache
    def last():
        file_name = DataItem.file_name
        item_list = {}
        with open(file_name, "r+") as openfile:
            item_list = json.load(openfile)
        serial_num = ([int(i) for i in item_list.keys()])
        return  str(max(serial_num))
    
    @classmethod
    def new_item(cls, item_type: str, serial: str):
        cls.item_type = item_type
        if len(serial) > DataItem.serial_length:
            raise PermissionError ("Serial number exceeds allowed number of digits")  
        else:
            serial = (DataItem.serial_length- len(serial)) * "0" + serial   
        cls.serial = serial
        item_list = {}
        cls.details_list = DataItem.details_list
        info_keys = dict.fromkeys(DataItem.item_info)
        info_keys["details"] = dict.fromkeys(DataItem.details_list[cls.item_type])
        info_keys["type"] = item_type
        info_keys["restrictions"] = dict.fromkeys(DataItem.restrictions[cls.item_type])        
        print(f"Starting item number: {cls.serial} | of type: {cls.item_type}")
        for info in info_keys.keys():
            if info == "type":
                continue
            if info_keys[info]:
                for specific in info_keys[info]:
                        info_keys[info][specific] = input(f"{info}: {specific}: ")
                continue
            else:
                info_keys[info] = input(f"{info}: ")
          
        item_list[cls.serial] = info_keys
        return item_list
    
class Storage():
    """A class to store all storage information"""
    # Defining the structure of the data item.
    # This can be changed and there is a function that will update the old data to the updated format.
    trans_info = ["serial", "type", "time_stamp", "item", "stor_loc", "action"]
    stock_info = ["item", "stor_item", "stor_loc", "quantity", "value"]

    transactions = "StorageData.json"
    stock = "StockData.json"
    serial_length = DataItem.serial_length
    
    def __init__(self):
        pass
    
    @staticmethod
    def item_format():
        return Storage.trans_info
    
    @functools.cache
    def current_loc(item):
        file_name = Storage.stock
        item_list = {}
        with open(file_name, "r+") as openfile:
            item_list = json.load(openfile)
        serial_num = ([int(i) for i in item_list.keys()])
        return  str(max(serial_num))
        
    
    @classmethod
    def transaction(cls, store_id: str, item_id: str, receive: str):
        cls.store_id = store_id
        cls.item_id = item_id
        cls.receive = receive
        
        transaction = {}
        cls.details_list = Storage.item_info

          
        item_list[self.serial] = info_keys
        return item_list        

