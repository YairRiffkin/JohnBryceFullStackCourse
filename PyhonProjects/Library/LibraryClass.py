import json
import functools
import datetime

class DataItem():
    """A class to define all attributes of a data item"""
    # Defining the structure of the data item.
    # This can be changed and there is a function that will update the old data to the updated format.
    item_info = ["type", "details", "location", "value"]
    details_list = {
                "book": ["title", "author", "genre", "language", "publication year"],
                "customer": ["family", "first", "address"],
                "employee": [],
                "library": ["title", "address"]
                }
    file_name = "ItemData.json"
    serial_length = 6
    
    def __init__(self):
        pass
    
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
    trans_info = ["type", "time_stamp", "item", "stor_loc", "action"]
    stock_info = ["stor_item", "stor_loc", "quantity", "value"]

    transactions = "StorageData.json"
    stock = "StockData.json"
    serial_length = DataItem.serial_length
    
    def __init__(self):
        with open(self.stock, "r") as openfile:
            self.stock_data = json.load(openfile)
        with open(self.transactions, "r") as openfile:
            self.storage_data = json.load(openfile)
            
    def print_data(self):
        print(self.stock_data)
    
    @staticmethod
    def item_format():
        return Storage.trans_info
    
    @classmethod
    def display_options(cls, options:list): 
        i = 0
        for choice in options:
            i += 1
            print(str(i), end = ".")
            if i < len(options) :
                print(choice.title(), end= " / ")
            else:
                print(choice, end= "")
        my_choice = input(" : choice? ")
        if my_choice.lower() in options:
            pass
        if my_choice.isdigit():
            if int(my_choice) > 0 and int(my_choice) <= i:
                my_choice = options[int(my_choice) - 1]
        elif my_choice:
            print("Incorrect input. Try again.")
        return my_choice    
        
    def stock_info(self, item_id: str) -> dict:
        stor_info = {}
        stor_loc = self.stock_data[item_id].keys()
        for loc in stor_loc:
            locations = list(self.stock_data[item_id][loc].keys())
            stor_info.update({loc: locations})   
        return stor_info
    
    
    def transaction(self, item_id: str, source: str, dest: str, quantity:float) -> dict:
        # get location and quantity information of item
        stor_info = self.stock_info(item_id)
        if len(stor_info[source]) == 1:
            loc = stor_info[source][0]
        else:
            #if item is in more than 1 location at source -> choose the location.
            print("Choose source location")
            loc = self.display_options(stor_info[source])
        # get item quantity at source
        source_quantity = float(self.stock_data[item_id][source][loc][0])
        source_value = float(self.stock_data[item_id][source][loc][1])
        unit_source_value = source_value / source_quantity
        source_quantity = source_quantity - quantity # Deduct transfer from source
        source_value = source_value - unit_source_value * quantity
        print("Choose destination location")
        options = stor_info[dest]
        options.append("New")
        print(options, type(options))
        dest_loc = self.display_options(options)
        if dest_loc.lower() == "new":
            dest_loc = input("Type new location name: ")
            self.stock_data[item_id][dest][dest_loc] = ["0", "0"]
        dest_quantity = float(self.stock_data[item_id][dest][dest_loc][0])
        dest_value = float(self.stock_data[item_id][dest][dest_loc][1])
        dest_quantity = dest_quantity + quantity
        dest_value = dest_value + unit_source_value * quantity
        # Register change in stock situation
        self.stock_data[item_id][source][loc]=[str(source_quantity), str(source_value)]
        self.stock_data[item_id][dest][dest_loc]=[str(dest_quantity), str(dest_value)]
        time_stamp = datetime.datetime.now()
        # register transactions in storage data file
        # time stamp is the identifier
        time_stamp = time_stamp.strftime("%d-%m-%Y %X")
        outgoing = {"serial": item_id, "storage": source, "bin": loc, "quantity": -1 * quantity, "value": -1 * unit_source_value * quantity}
        ingoing = {"serial": item_id, "storage": dest, "bin": dest_loc, "quantity": quantity, "value": unit_source_value * quantity}
        transaction = {"output": outgoing, "input": ingoing}
        self.storage_data[time_stamp] = transaction
        with open(self.stock, 'w') as outfile:
            json.dump(self.stock_data, outfile, sort_keys= True, indent= 4)
        with open(self.transactions, 'w') as outfile:
            json.dump(self.storage_data, outfile, sort_keys= True, indent= 4)
        
        
        
       

          
           

