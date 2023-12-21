import json
import functools
import datetime
from tabulate import tabulate

class DataItem():
    """A class to define all attributes of a data item"""
    # Defining the structure of the data item.
    # This can be changed and there is a function that will update the old data to the updated format.
    
    item_info = ["type", "details", "location", "value"] #essential item attributes
    # deatils to be added per type to details attribute
    details_list = {
                "book": ["title", "author", "genre", "language", "publication year", "class"],
                "customer": ["family", "first", "address"],
                "employee": [],
                "library": ["title", "address"]
                }
    # Essentials to be compared when chscking for duplicates (also the headers for display item tables)
    duplicate_list = {
                "book": ["author", "title"],
                "customer": ["family", "first"],
                "employee": ["family", "first"],
                "library": ["address"]
                }
    file_name = "ItemData.json"
    serial_length = 6
    # restrictions on max. loan days for books
    class_restrict = {"1": 10, "2": 5, "3": 2}
    
    def __init__(self):
        with open(self.file_name, "r") as openfile:
            self.item_data = json.load(openfile)
    
    def update_list(self, new_dict: dict) -> json:
        """Update item data list"""
        with open(self.file_name, 'w') as outfile:
            json.dump(new_dict, outfile, sort_keys= True, indent= 4)
        
    def get_item(self, serial: str = "") -> dict:
        """ Get specific item details from item ID"""
        if serial == "":
            return self.item_data
        else:
            self.item = self.item_data[serial]
            return self.item
        
    def next_serial(self) -> list:
        """Returns max. serial number & next serial for new item"""
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
                    
    def display_list(self, item_list: dict, item_type:str, sort_item: str = "", option:str = "", deleted: bool = False) -> list:       
        """Method for sorting a list of "item type" option to print table"""
        # "item list": dict to be displayed
        # "item type": type of item for header display
        # "sort item": by dict key. Default by first detail in self.duplicate list
        # "option": "any" - no print, "print" - print tabulated table according to duplicate list in class header
        # "deleted": allows display of deleted item with the initial type
        if sort_item == "":
            sort_item = self.duplicate_list[item_type][0] # if no sort is chosen sort is by first detail in details
        def myFunc(e):
            return e[sort_item]
        display_item_list = [] # list of dict - to allow sort function
        sort_list = {}
        for i in item_list:
            if deleted:
                if item_type.lower() in item_list[i]["type"].lower(): #"in" operator instead of "=="
                    sort_list = {"ID": i}
                    details = item_list[i]["details"]                    
                    sort_list.update(details)
                    display_item_list.append(sort_list)
            else:
                if item_type == item_list[i]["type"]:
                    sort_list = {"ID": i}
                    details = item_list[i]["details"]                    
                    sort_list.update(details)
                    display_item_list.append(sort_list)
        # display_item_list.sort(key= myFunc) # sorted list of dict
        # tabulated table print module
        header = ["ID"]
        header.extend(self.duplicate_list[item_type])
        print_item_list = []
        for i in display_item_list: # process each dict in list seperately
            short_list = []
            short_list.append(i["ID"])
            for n in i:
                 if n in self.duplicate_list[item_type]:
                    short_list.append(i[n]) # collect relevant keys into list for each line in table
            print_item_list.append(short_list) # list of lists for tabulate class
        if option == "print":
            print(tabulate(print_item_list, headers= header))
        self.header = header
        self.print_item_list = print_item_list #list of list => printed items
        return [self.print_item_list, header]
    
    def find_item(self, item_type: str, choose: bool = False) -> list:
        """ Method to search item in list by attributes and create a choice list as option"""
        # analogy table of dict format and choice option
        # "choose" allows choice from list
        options = {
            "book": 
               [["ID", "TITLE", "AUTHOR"], ["ID", "title", "author"]],
            "customer":
                [["ID", "SURNAME", "FIRST NAME"], ["ID", "family", "first"]]
        }
        result = []
        search_loop = True
        # item_list = self.display_list(item_type)
        while search_loop:
            search_list = {}
            print("How would you like to search") #attribute to search by
            option_list = options[item_type][0]
            x = Storage.display_options(option_list)
            text_result = option_list[x]
            what_to_search = input(f"Input what to search in {text_result.title()}: ") #any string in search attribute
            
            search_key = options[item_type][1][x]
            for index in self.item_data:
                if self.item_data[index]["type"] == item_type:
                    if search_key == "ID":
                        if what_to_search in index:
                            search_list[index] = self.item_data[index]
                    else:
                        if what_to_search in self.item_data[index]["details"][search_key]:
                            search_list[index] = self.item_data[index]
            choose_display = self.display_list(search_list, item_type)
            
            if not search_list: #if search list is empty
                empty = True
                print(f"No {item_type.upper()} found.")
            if choose:
                spacer = []
                header = choose_display[1]
                for  detail in header:
                    spacer.append("")
                display_list = choose_display[0]
                display_list.append(["Retry"])
                display_list.append(["Quit"])
                
                result = Storage.display_options(display_list, header)
                if display_list[result][0].lower() == "retry":
                    search_loop = True
                elif display_list[result][0].lower() == "quit":
                    search_loop = False
                    print("Returning to main menu")
                    result = []
                else:
                    search_loop = False
                    result = {display_list[result][0]: search_list[display_list[result][0]]}
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
                if details == "class": data = "1"
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
                        data = input(f"{key} | {detail}: ")
                        if detail == "class":
                            if data not in ("1", "2", "3"):
                                print("Must be 1, 2 or 3")
                                data = "retry"
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
                    if key == "value":
                        try:
                            try_value = float(data)
                        except:
                            if data == "": continue
                            else:
                                print("number is required")
                                data = "retry"
                    if data == "": 
                        data = self.default(item_type, key, detail)
                        if data == "retry": 
                            print("Sorry, data is compulsory")
                item_list.update({key: data})
        duplicate = self.compare(item_list)
        found_item = {}
        if duplicate[0]: # type: ignore
            found = "similar"
            option = "Add new item"
            if duplicate[1]:  # type: ignore
                found = "deleted"
                option = "Restore"
            print(f"""Found {found} "{item_type.upper()}" item:""")
            found_item[duplicate[2]] = self.item_data[duplicate[2]] # type: ignore
            d = self.display_list(found_item, item_type, "", "print", duplicate[1])
            print("What would you like to do?")
            x = [option, "Abort"]
            choice = Storage.display_options(x) + 1
            if choice == 1:
                self.item_data[serial] = item_list
                self.update_list(self.item_data)
            else:
                print("Aborting new item")
    
    def delete_item(self, serial: str) -> None:
        """Delete item by changing type to "delete" + cureent type"""
        item = {serial: self.get_item(serial)}
        item_type = item[serial]["type"]
        print(f"Deleting item: {serial}{"\t"}Type: {item_type.title()}")
        x = self.display_list(item, item_type, "", "print")
        x = input("Are you sure? (Y/N)? ")
        if x.lower() == "y":
            self.item_data[serial]["type"] = "deleted - " + self.item_data[serial]["type"].upper()
            self.update_list(self.item_data) 
            return(self.item_data)
        else:
            print("Aborting Delete")
        
        
    def compare(self, item_info: dict) -> any:
        """Check if item already exists"""
        #Check by details defined in "duplicate_list" in class header
        item_type = item_info["type"]
        details = item_info["details"]
        data = False
        duplicate = False
        deleted = False
        serial = ""
        found_item = {}
        for i in self.item_data:
            compared_type = self.item_data[i]["type"]
            if item_type.lower() in compared_type.lower():
                if "deleted" in compared_type:
                    deleted = True
                for check in self.duplicate_list[item_type]:
                    if self.item_data[i]["details"][check].lower() == details[check].lower():
                        duplicate = True
                        serial = i.zfill(self.serial_length)
                    else:
                        duplicate = False
        return [duplicate, deleted, serial] # type: ignore
                    
                    
   
class Storage():
    """A class to store all storage information"""

    transactions = "StorageData.json"
    stock = "StockData.json"
    serial_length = DataItem.serial_length
    date_format = "%d-%m-%Y %X"
    
    def __init__(self):
        with open(self.stock, "r") as openfile:
            self.stock_data = json.load(openfile)
        with open(self.transactions, "r") as openfile:
            self.storage_data = json.load(openfile)
            
    def print_data(self):
        print(self.stock_data)
    
    @classmethod
    def display_options(cls, options: any, header: list = []) -> int: 
        if header:
            header_addition = ["#"]
            header_addition.extend(header)
        i = 1
        print_options = []
        for item in options:
            if type(item) == str:
                item = [item]
            line = [i]
            line.extend(item)
            print_options.append(line)
            i += 1
        input_loop = True
        while input_loop:
            print(tabulate(print_options, headers= header))         
            my_choice = input(f"{"\n"}CHOICE? ")
            if my_choice.isdigit():
                if int(my_choice) > 0 and int(my_choice) <= len(options):
                    answer = int(my_choice) - 1
                    input_loop = False
            else:
                print("Incorrect input. Try again.")
        return answer    
        
    def stock_info(self, item_id: str) -> dict:
        """Check if item is in stock"""        
        stor_info = False
        if item_id in self.stock_data.keys():
            stor_info = True             
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
        if possible: 
            unit_source_value = value
            source_value = unit_source_value * source_quantity
            try:
                dest_quantity = float(self.stock_data[item_id][dest][0])
                dest_value = float(self.stock_data[item_id][dest][1])
            except:
                dest_quantity = float(0)
                dest_value = float(0)      
              
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
            time_stamp = time_stamp.strftime(self.date_format)
            outgoing = {"serial": item_id, "storage": source, "quantity": -1 * quantity, "value": -1 * unit_source_value * quantity}
            ingoing = {"serial": item_id, "storage": dest, "quantity": quantity, "value": unit_source_value * quantity}
            transaction = {"output": outgoing, "input": ingoing}
            self.storage_data[time_stamp] = transaction
            with open(self.stock, 'w') as outfile:
                json.dump(self.stock_data, outfile, sort_keys= True, indent= 4)
            with open(self.transactions, 'w') as outfile:
                json.dump(self.storage_data, outfile, sort_keys= True, indent= 4)
        
    def last_transaction(self, loc: str, serial: str, in_out= "input") -> str:
        """ method to get last transaction in specific location"""
        # loc: location
        # serial: item ID
        # in_out: choose if to get incoming or outgoing transaction
        trans_list = []
        for i in self.storage_data:
            x = self.storage_data[i][in_out]["storage"]
            y = self.storage_data[i][in_out]["serial"]
            if x == loc and y == serial:
                trans_list.append(i)
        if trans_list: # checking for error in data base due to project tests    
            self.last = max(trans_list)
        else:
            self.last = datetime.datetime.now()
            self.last = str(self.last.strftime("%d-%m-%Y %X"))
        return self.last
           
    def item_stock(self, overdue: bool = False, loc_type: str = "customer", item_type: str = "book") -> any:
        """Method to list item status in storage"""  
        # overdue -> prints only overdue books
        
        item_list = DataItem() 
        header_dict = DataItem.duplicate_list #print details from DataItem class
        item_in_loc = {}
        class_restrict = {1: 10, 2: 5, 3: 2}
        # extracting data => item location as key and items in location as details
        # this requires reversing the StockData file
        for serial in self.stock_data:
            loc_data = item_list.get_item(serial)
            if loc_data["type"] == item_type:
                
                loc_for_item = self.stock_data[serial].keys()
                for location in loc_for_item:
                    print(location)
                    if item_type == "book" and overdue:
                        now_time = datetime.datetime.now()
                        item_class = int(item_list.get_item(serial)["details"]["class"])
                        max_days = class_restrict[item_class]
                        time_stamp = self.last_transaction(location, serial)
                        time_stamp = datetime.datetime.strptime(time_stamp, self.date_format)
                        time_passed = int((now_time - time_stamp).days)
                        if time_passed <= max_days:
                            continue
                    try: # check location exists 
                        loc_data = item_list.get_item(location)
                        if loc_data["type"] == loc_type:
                            try:
                                check = item_in_loc[location] # if there is already an item in location
                                item_in_loc[location].append(serial) # collect stored item into storage item
                            except:
                                item_in_loc[location] = [serial] # for first instance of item in location
                    except:
                        continue
        result = [] # output list
        header = []
        for item in item_in_loc: # creating list of lists for tabulate table
            additional_line = [""]
            for i in range(len(item_in_loc[item])):
                line = [] # List in "result" for table
                if i == 0: # if multiple items in location => location details will apear only in first line
                    line.append(item)
                    for n in header_dict[loc_type]: # location details from DataItem class
                        line.append(item_list.get_item(item)["details"][n])
                        additional_line.append("")
                else: # empty string for all line except first
                    line.extend(additional_line)
                line.append(item_in_loc[item][i])
                for n in header_dict[item_type]: # item details from DataItam class
                    line.append(item_list.get_item(item_in_loc[item][i])["details"][n])
                if item_type == "book":
                    now_time = datetime.datetime.now()
                    item_class = int(item_list.get_item(item_in_loc[item][i])["details"]["class"])
                    max_days = class_restrict[item_class]
                    time_stamp = self.last_transaction(item, item_in_loc[item][i])
                    time_stamp = datetime.datetime.strptime(time_stamp, self.date_format)
                    time_passed = int((now_time - time_stamp).days)
                    if time_passed > max_days:
                        loan_status = f"Overdue [{max_days} | {time_passed}]"
                    else:
                        loan_status = "" 
                    # status1 = max_days
                    # status2 = time_passed
                    # line.append(status1)
                    # line.append(status2)
                    line.append(loan_status)                        
                result.append(line)
        # Creating header for tabulate table
        header.append("ID")
        header.extend(header_dict[loc_type])
        header.append("ID")
        header.extend(header_dict[item_type])
        if item_type == "book":
            # header.append("Max Days")
            # header.append("Act. Days")
            header.append("Status [M | A]")
        print(tabulate(result, headers= header))
        return result                    
            
            
        
       

          
           

