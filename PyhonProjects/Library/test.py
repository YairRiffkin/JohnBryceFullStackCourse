import json

#input book
detail_list = {"book": ["title", "author", "genre", "language", "publication year", "location", "value"], "customer": [1, 2], "employee": []}
# print(detail_listst["book"])
def new_item():
    details = {}
    item_list = {}
    print("Choose item type to input: ")
    for choice in detail_list.keys():
        print(choice, end= " / ")
    my_choice = input(" : choice?: ")
    serial = input("Serial number: ")
    item_list.update({"type": my_choice, "code": serial})
    for detail in detail_list[my_choice]:
        x = input(str(detail).title() + " : ")
        details.update({detail: x})
    item_list.update({"details": details})
    return item_list    

x = new_item()
y = json.dumps(x, indent= 4)
with open("ItemData.json", "w") as json_file:
    json.dump(y, json_file)
# print(y)

# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)