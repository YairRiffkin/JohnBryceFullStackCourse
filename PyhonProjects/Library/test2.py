# import json
# file_name = "ItemData.json"
# with open(file_name, "r") as openfile:
#     item_list = json.load(openfile)
#     print(item_list.keys())
#     max_serial = ([int(i) for i in item_list.keys()])
#     print(max_serial)
#     max_serial = max(max_serial)
#     print(max_serial)
# print(item_list)


import json
import LibraryClass as lc
with open(lc.DataItem.file_name, "r+") as openfile:
            item_list = json.load(openfile)
print(item_list)
x = {"8": "sdfsfd"}
item_list.update(x)
print(item_list)