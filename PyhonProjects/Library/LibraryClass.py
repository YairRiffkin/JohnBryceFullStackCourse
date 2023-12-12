import json
import functools
import datetime

class DataItem():
    """A class to define all attributes of a data item"""
    # Defining the structure of the data item.
    # This can be changed and there is a function that will update the old data to the updated format.
    item_info = ["type", "details", "location", "value"]
    details_list = {
                "book": ["title", "author", "genre", "language", "publication year", "class"],
                "customer": ["family", "first", "address"],
                "employee": [],
                "library": ["title", "address"]
                }
    duplicate_list = {
                "book": ["title", "author"],
                "customer": ["family", "first"],
                "employee": ["family", "first"],
                "library": ["address"]
                }
    file_name = "ItemData.json"
    serial_length = 6
    class_restrict = {"1": 10, "2": 5, "3": 2}
    
    def __init__(self):
        with open(self.file_name, "r") as openfile:
            self.item_data = json.load(openfile)
    
    def update_list(self, new_dict: dict) -> json:
        """Update item data list"""
        with open(self.file_name, 'w') as outfile:
            json.dump(new_dict, outfile, sort_keys= True, indent= 4)
        
    def get_item(self, serial):
        self.item = self.item_data[serial]
        return self.item
        
    def next_serial(self) -> list:
        """Calculates current max. serial number and the next serial number one for new items"""
        serial_list = self.item_data.keys()
        self.max_serial = max(serial_list)
        self.next_ser = str(int(self.max_serial) + 1).zfill(self.serial_length)
        return [self.max_serial, self.next_ser]
        
    def average_value(self, item_type: str) -> str:
        """Calculate average value for an item type"""
        round_digit = 4
        average_val = 0
        count_item = 0
        for i in self.item_data:
            if self.item_data[i]["type"] == item_type:
                if self.item_data[i]["value"]:
                    average_val = average_val + float(self.item_data[i]["value"])
                    count_item += 1
        self.average_val = str(round(average_val / count_item, round_digit))
        return self.average_val
                    
    def display_list(self, item_type, sort_item = "", option = "", specific = ""):       
        if sort_item == "":
            sort_item = self.duplicate_list[item_type][0]
        def myFunc(e):
            return e[sort_item]
        display_item_list = []
        sort_list = {}
        item_list = []
        short_list = ""
        value_max_len = dict.fromkeys(self.duplicate_list[item_type], 0)
        for i in self.item_data:
            if specific:
                if i != specific: 
                    continue
            if self.item_data[i]["type"] == item_type:
                sort_list = {"ID": i}
                item = self.item_data[i]["details"]
                for key_index in item.keys():
                    if key_index in value_max_len.keys():
                        if len(item[key_index]) > value_max_len[key_index]:
                            value_max_len[key_index] = len(item[key_index])                    
                sort_list.update(item)
                display_item_list.append(sort_list)
        display_item_list.sort(key= myFunc)
        for i in display_item_list:
            short_list = "ID: " + str(i["ID"] + " ")
            for n in i:
                if n in self.duplicate_list[item_type]:
                    item_lemgth = len(i[n])
                    spacer = (value_max_len[n] - item_lemgth + 2) * " "
                    short_list = short_list + str(n) + ": " + str(i[n]) + spacer
            item_list.append(short_list)
        self.item_list = item_list
        if option == "print":
            for i in self.item_list:
                print(i)
        return self.item_list
    
    def find_item(self, item_type, choose= False):
        options = {
            "book": 
                (["id", "title", "author"], ["id", "title", "author"]),
            "customer":
                (["id", "surename", "first name"], ["id", "family", "first"])
        }
        result = []
        search_loop = True
        item_list = self.display_list(item_type)
        while search_loop:
            search_list = []
            empty = False
            print("How would you like to search")
            x = Storage.display_options(options[item_type][0])
            what_to_search = input(f"Input what to search in {x[1]}: ")
            # if what_to_search == "": what_to_search = " "
            search_key = options[item_type][1][int(x[0])-1] + ":"
            for index in item_list:
                search_line = index.lower()
                search_split = search_line.split()
                search_string = search_split.index(search_key) + 1
                if what_to_search in search_split[search_string]:
                    search_list.append(index)
            if (len(search_list)) == 0: empty = True
            if choose:
                search_list.append("retry?")
                search_list.append("quit")
                x = Storage.display_options(search_list)
                if x[1].lower() == "retry?":
                    search_loop = True
                else:
                    if empty:
                        search_loop = False
                        result = [False]
                    else:
                        search_loop = False
                        result = x[1][4 : 4 + self.serial_length]
            else:
                search_loop = False
                result = search_list
        self.result = result
        return self.result
                                        
    
    def default(self, item_type: str, item_key: str, details: str):
        """Checks which details are "must" and/or create default"""
        data = ""
        if item_type == "customer":
            if item_key == "location": data = "address"
            elif item_key == "value": data = ""
            elif item_key == "details": data = "retry"
        elif item_type == "book":
            if item_key == "location": data = ""
            elif item_key == "value": data = self.average_value("book")
            elif item_key == "details":
                if details == "class": data = str(self.class_restrict["1"])
                else: data = "retry"
        else:
            pass
        self.data = data
        return self.data
               
        
    
    def new_item(self, item_type: str) -> dict:
        """Input new item information"""
        serial = self.next_serial()[1]
        item_list = {}
        info_keys = dict.fromkeys(DataItem.item_info)
        info_keys["details"] = dict.fromkeys(DataItem.details_list[item_type])
        # info_keys["type"] = item_type
        print(f"Starting item number: {serial} | of type: {item_type} =>")
        for key in info_keys.keys():
            if key == "type":
                item_list.update({"type": item_type})
                continue
            if info_keys[key]:
                detail_data = {}
                for detail in info_keys[key].keys():
                    data = "retry"
                    while data == "retry":
                        ###############################################
                        data = input(f"{key} | {detail}: ")
                        if data == "": 
                            data = self.default(item_type, key, detail)
                            if data == "retry": 
                                print("Sorry, data is compulsory")
                    detail_data.update({detail: data})
                    item_list.update({key: detail_data})
            else:
                data = "retry"
                while data == "retry":
                    data = input(f"{key}: ")
                    if data == "": 
                        data = self.default(item_type, key, detail)
                        if data == "retry": 
                            print("Sorry, data is compulsory")
                item_list.update({key: data})
        duplicate = self.compare(item_list)
        if duplicate:
            print("Aborting new item")
        else:
            self.item_data[serial] = item_list
            self.update_list(self.item_data)
    
    def delete_item(self, serial):
        item = self.item_data[serial]
        print(item)
        print(item.keys())
        print(f"Deleting item: {serial}{"\t"}Type: {self.item_data[serial]["type"]}")
        for i in item["details"].keys():
            # print(f"{i}")
            print(f"{i}:{"\t"}{item["details"][i]}")
        x = input("Are you sure? (Y/N)? ")
        if x.lower() == "y":
            self.item_data[serial]["type"] = "deleted - " + self.item_data[serial]["type"].upper()
        else:
            print("Aborting Delete")
            exit()
        self.update_list(self.item_data)  
        
    def compare(self, item_info: dict):
        item_type = item_info["type"]
        details = item_info["details"]
        data = False
        duplicate = False
        serial = ""
        for i in self.item_data:
            if self.item_data[i]["type"] == item_type:
                for check in self.duplicate_list[item_type]:
                    if self.item_data[i]["details"][check].lower() == details[check].lower():
                        duplicate = True
                        serial = i.zfill(self.serial_length)
                    else:
                        duplicate = False
        if duplicate:
            print(f"""Found similar "{item_type.upper()}" item:""")
            print(serial, self.item_data[serial])
            print("What would you like to do?")
            x = ["add new item", "abort"]
            x = Storage.display_options(x)
            choice = int(x[0])
            if choice == 1:
                data = False
            else:
                data = True
        return data
                    
                    
   
class Storage():
    """A class to store all storage information"""
    trans_info = ["time_stamp", "item"]
    stock_info = ["quantity", "value"]

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
    
    # @staticmethod
    # def item_format():
    #     return Storage.trans_info
    
    @classmethod
    def display_options(cls, options:list, ending= "\n"): 
        text_answer = ["", ""]        
        input_loop = True
        while input_loop:
            i = 0
            for choice in options:
                options[i] = options[i].lower()
                i += 1
                print(str(i), end = ") ")
                if i < len(options) :
                    print(choice.title(), end= ending)
                else:
                    print(choice.title(), end= "")
            
            my_choice = input(f"{"\n"}CHOICE? ")
            if my_choice.lower() in options and my_choice != "":
                text_answer[1] = my_choice
                text_answer[0] = str(int(options.index(my_choice.lower()))+1)
                input_loop = False
            elif my_choice.isdigit():
                if int(my_choice) > 0 and int(my_choice) <= i:
                    text_answer[1] = options[int(my_choice) - 1]
                    text_answer[0] = str(int(my_choice))
                    input_loop = False
            else:
                print("Incorrect input. Try again.")
        return text_answer    
        
    def stock_info(self, item_id: str) -> dict:
        stor_info = False
        if item_id in self.stock_data.keys():
            stor_info = True               
        self.store_info = stor_info
        return stor_info
    
    
    def transaction(self, item_id: str, source: str, dest: str, quantity:float, value: float = 1) -> dict:
        # get item quantity at source
        possible = True
        try:
            source_quantity = float(self.stock_data[item_id][source][0])
            source_value = float(self.stock_data[item_id][source][1])
            unit_source_value = source_value / source_quantity
        except:
            if source == "":
                source_quantity = float(quantity)
            else:
                possible = False
                print("Item does not exist in source")
            unit_source_value = value
            source_value = unit_source_value * source_quantity
        try:
            dest_quantity = float(self.stock_data[item_id][dest][0])
            dest_value = float(self.stock_data[item_id][dest][1])
        except:
            dest_quantity = float(0)
            dest_value = float(0)      
        
        if possible:           
            source_quantity = source_quantity - quantity # Deduct transfer from source
            source_value = source_value - unit_source_value * quantity        
            
            dest_quantity = dest_quantity + quantity
            dest_value = dest_value + unit_source_value * quantity
            # Register change in stock situation
            self.stock_data[item_id][source]=[str(source_quantity), str(source_value)]
            self.stock_data[item_id][dest]=[str(dest_quantity), str(dest_value)]
            time_stamp = datetime.datetime.now()
            # register transactions in storage data file
            # time stamp is the identifier
            time_stamp = time_stamp.strftime("%d-%m-%Y %X")
            outgoing = {"serial": item_id, "storage": source, "quantity": -1 * quantity, "value": -1 * unit_source_value * quantity}
            ingoing = {"serial": item_id, "storage": dest, "quantity": quantity, "value": unit_source_value * quantity}
            transaction = {"output": outgoing, "input": ingoing}
            self.storage_data[time_stamp] = transaction
            with open(self.stock, 'w') as outfile:
                json.dump(self.stock_data, outfile, sort_keys= True, indent= 4)
            with open(self.transactions, 'w') as outfile:
                json.dump(self.storage_data, outfile, sort_keys= True, indent= 4)
        
        
        
       

          
           

