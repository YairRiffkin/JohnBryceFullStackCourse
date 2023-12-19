import json
import LibraryClass as lc
import os


project_assignment = [
"Add a new customer", 
"Add a new book", 
"Loan a book", 
"Return a book", 
"Display all books", 
"Display all customers", 
"Display all loans", 
"Display late loans", 
"Find book by name", 
"Find customer by name", 
"Remove book", 
"Remove customer", 
"Exit system"]


item_data = lc.DataItem()
storage = lc.Storage()

def clear_screen():
    os.system('cls')

def pick_options(pick: int, choice= [], option= []):
    x = False
    y = []
    for i in zip(choice, option):
        if pick == i[0]:
            x = True
            y = i[1]
    return [x, y]
            
        
search_memory = ""    
while True:   
    option = True 
    clear_screen()
    print("OPTIONS MENU: ")
    print("=================")
    # print_list = list(enumerate(project_assignment, 1))
    choice = lc.Storage.display_options(project_assignment) + 1
    clear_screen()

    choice_check = pick_options(choice, [1, 2], ["customer", "book"])
    if choice_check[0]:
        item = choice_check[1]
        while option:  
            clear_screen() 
            print(f"ADD A NEW {item.upper()}", "\n")
            item_data.new_item(item)
            x = input(f"Would you like to add another {item}? (Y/N) ")
            if x.lower() != "y":
                option = False
    
    
    
    choice_check = pick_options(choice, [3, 4], ["book", "book"])
    # 3 -> dest = customer, 4 -> dest = library
    if choice_check[0]:
        while option: 
            print("[LOAN] or [RETURN] A BOOK")
            item = choice_check[1]
            print("Customer Details ==>")
            customer = item_data.find_item("customer", True)
            if not customer:
                continue                
            clear_screen()
            print("Book Details ==>")
            book = item_data.find_item("book", True)
            if not book:
                continue
            clear_screen()
            print(project_assignment[choice-1].upper())
            print("BOOK: ")
            x = item_data.display_list(book, "book", "", "print")
            book_id = x[0][0][0]
            print("CUSTOMER: ")
            x = item_data.display_list(customer, "customer", "", "print")
            customer_id = x[0][0][0]
            x = input("Continue? (Y/N) ")
            if x.lower() == "y":
                if choice == 3:
                    source = "000001"
                    dest = customer_id
                if choice == 4:
                    source = customer_id
                    dest = "000001"
                item_value = item_data.get_item(book_id)
                value = float(item_value["value"])
                storage.transaction(book_id, source, dest, 1, value)
            x = input(f"Would you like to add another {item}? (Y/N)")
            if x.lower() != "y":
                option = False    
    
    choice_check = pick_options(choice, [5, 6], ["book", "customer"])
    if choice_check[0]:
        while option:
            print(f"DISPLAYING ALL {choice_check[1].upper()}S: ")
            x = item_data.get_item() 
            y = item_data.display_list(x, choice_check[1], "", "print")   
            x = input("Continue? (Y/N) ")
            if x.lower() != "n":
                option = False    
                
    choice_check = pick_options(choice, [7, 8], ["", ""])
    if choice_check[0]:
        while option:
            overdue = False
            print(f"{project_assignment[choice - 1].upper()}: ")
            if choice == 8:
                overdue = True 
            storage.item_stock(overdue)
            x = input("Continue? (Y/N) ")
            if x.lower() != "y":
                option = False
                
    choice_check = pick_options(choice, [9, 10], ["book", "customer"])
    if choice_check[0]:
        while option:
            print(choice_check[1])
            print(f"FIND {choice_check[1].upper()} BY DETAIL")
            print("Search will allow partial detail (even 1 letter or digit will suffice)")
            search_memory = item_data.find_item(choice_check[1], True)
            if search_memory:
                search_memory = list(search_memory.keys())[0]
            x = input("Continue? (Y/N) ")
            if x.lower() != "y":
                option = False
    
    choice_check = pick_options(choice, [11, 12], ["book", "customer"])
    if choice_check[0]:
        while option:
            serial = ""
            clear_screen()
            if search_memory:
                x = input(f" Would you like to use item number {search_memory} from last search? (Y/N) ")
                if x.lower() == "y":
                    serial = search_memory
                else:
                    serial = input(f"{project_assignment[choice - 1].upper()} with serial number: ")
            else:
                serial = input(f"{project_assignment[choice - 1].upper()} with serial number: ")            
            serial = serial.zfill(lc.DataItem.serial_length)
            print(serial)
            try:
                check_serial = item_data.get_item(serial)
                if check_serial["type"] == choice_check[1]:
                    delete_data = item_data.delete_item(serial)
                    if delete_data:
                        search_memory = list(delete_data.keys())[0]
                else:
                    print(f"{serial} is not of type {choice_check[1].upper()}")
            except:
                print(f"item {serial} does not exist")              
            
            x = input("Continue? (Y/N) ")
            if x.lower() != "y":
                option = False    
            
            
        
    #         x = input("Continue? (Y/N) ")
    #         if x.lower() != "n":
    #             option = False
            




