import json
import LibraryClass as lc
with open(lc.DataItem.file_name, "r") as openfile:
    item_list = json.load(openfile)
with open(lc.Storage.transactions, "r") as openfile:
    transactions = json.load(openfile)
# with open(lc.Storage.stock, "r") as openfile:
#     stock = json.load(openfile)



x = lc.Storage()
x.print_data()
print(x.stock_info("000024"))

x.transaction("000024", "000001", "000004", 1)
x.print_data()