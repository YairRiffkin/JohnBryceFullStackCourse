import json
#input book
# detail_list = {"book": ["title", "author", "genre", "language", "publication year", "location", "value"], "customer": [1, 2], "employee": []}
detail_list = {"book": ["title", "author"], "customer": [1, 2], "employee": []}
# print(detail_listst["book"])
def new_item():
    with open("ItemData.json", "r") as openfile:
        item_list = json.load(openfile)
    # item_list = {}
    details = {}
    item_details = {}
    print("Choose item type to input: ")
    for choice in detail_list.keys():
        print(choice, end= " / ")
    my_choice = input(" : choice?: ")
    serial = input("Serial number: ")
    # item_list.update({"code": serial, "type": my_choice})
    for detail in detail_list[my_choice]:
        x = input(str(detail).title() + " : ")
        details.update({detail: x})
    # item_details = {"type": my_choice,  "details": details}
    item_details.update({serial: {"type": my_choice, "details": details}})
    item_list.update(item_details)
    return item_list    

x = new_item()
y = json.dumps(x, indent= 4)
with open("ItemData.json", "w") as json_file:
    json_file.write(y)
# print(y)

# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)