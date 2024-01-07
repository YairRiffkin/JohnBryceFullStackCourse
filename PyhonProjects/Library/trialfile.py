import json
import LibraryClass as lc
import os
import time
from pprint import pprint
from tabulate import tabulate
import datetime
import random

item = lc.DataItem()
stor = lc.Storage()

import json
file_name = "StockData.json"
with open(file_name, "r") as openfile:
    stock_list = json.load(openfile)
    
file_name = "StorageData.json"
with open(file_name, "r") as openfile:
    storage = json.load(openfile)    

list_of_items = item.get_item("000040")
f = item.get_item()
# print(list_of_items)
# b = list_of_items["details"]
# print(b)
x = item.compare(list_of_items)
print(x)
# print(list_of_items["type"])
# for index in item.duplicate_list["book"]:
#     c = b[index]
#     print(c == f["000040"]["details"][index])
    
    # if self.item_data[i]["details"][check].lower() == details[check].lower():


