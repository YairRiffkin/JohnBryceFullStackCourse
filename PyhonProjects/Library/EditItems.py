import json
import random

details_list = {
                "book": ["title", "author", "genre", "language", "publication year", "class"],
                "customer": ["family", "first", "address"],
                "employee": [],
                "library": ["title", "address"]
                }

file_name = "ItemData.json"
with open(file_name, "r") as openfile:
    new_file = json.load(openfile)
x = {}    
for i in new_file:
    # try:
    #     print(i, new_file[i]["location"])
    # except:
    #     print(i, new_file[i]["type"])
    if new_file[i]["type"] == "book":
        new_file[i]["location"] = ""
# x = json.dumps(new_file, sort_keys= True, indent= 4)
# print(x)
    
# Adjust "details"    
# for i in new_file.keys():
#     new_type = new_file[i]["type"]
#     new_details = details_list[new_type]
#     details = new_file[i]["details"]     
#     # print(new_type, len(new_details))
#     new_dict = {}
#     if len(new_details) == len(details):
#         for n in range(len(new_details)):            
#                 new_dict.update({new_details[n]: details[n]})
#     else:
#         for n in range(len(new_details)-1):            
#                 new_dict.update({new_details[n]: details[n]})               
#         x = random.choice([1, 2, 3])
#         new_dict.update({"class": x})        
#     new_file[i].update({"details": new_dict})

# Turn integer to string
# for i in new_file.keys():
#     if new_file[i]["type"] == "book":
#         x = new_file[i]["details"]["class"]
#         new_file[i]["details"]["class"] = str(x)
# print(new_file)

# put all books in library 1
# stock = {}
# for i in new_file.keys():
#     if new_file[i]["type"] == "book":
#         x = new_file[i]["value"]
#         stock.update({i: {"000001": ["1.0", str(x)]}})
# print(stock)

# with open("StockData.json", 'w') as outfile:
#     json.dump(stock, outfile, sort_keys= True, indent= 4)

# with open("ItemData.json", 'w') as outfile:
#     json.dump(new_file, outfile, sort_keys= True, indent= 4)
            
    

