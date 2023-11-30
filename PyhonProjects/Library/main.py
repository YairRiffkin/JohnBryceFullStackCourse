import json
import LibraryClass as lc
with open(lc.DataItem.file_name, "r+") as openfile:
            item_list = json.load(openfile)

def input_item():
    """Input new data item into system"""
    item_format = list(lc.DataItem.item_format())
    last_number = lc.DataItem.last()
    # item = lc.DataItem()
    first_entry = True
    my_choice = True
    while my_choice:
        print("Choose item type to input: ")
        i = 0
        for choice in item_format:
            i += 1
            print(str(i), end = ".")
            if i < len(item_format) :
                print(choice.title(), end= " / ")
            else:
                print(choice, end= "")
        my_choice = input(" : choice? ")
        if my_choice.lower() in item_format:
            pass
        if my_choice.isdigit():
            if int(my_choice) > 0 and int(my_choice) <= i:
                my_choice = item_format[int(my_choice) - 1]
        elif my_choice:
            print("Incorrect input. Try again.")
            my_choice = None
            print(my_choice)
    print(my_choice, last_number)
    new_item = lc.DataItem.new_item(my_choice, str(int(last_number) + 1))
    return new_item

    
new_item = input_item()  
print(type(new_item), type(item_list))
item_list.update(new_item)
print(item_list)