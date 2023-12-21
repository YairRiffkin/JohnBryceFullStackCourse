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
    """Checking user input Return list - digit (choice) and str (item type)"""
    choice_check = False
    item_choice = []
    for i in zip(choice, option):
        if pick == i[0]:
            choice_check = True
            item_choice = i[1]
    return [choice_check, item_choice]

def end_check(input_string: str = "Repeat?") -> bool:
    # question in string should direct answer "Y" to repeat last function. Other => return to menu
    option = True
    answer = input(input_string + " (Y/N) ")
    if answer.lower() != "y":
        option = False
    return option
            

                   
search_memory = "" #remebers search choice for other use  
continue_user = True 

while continue_user:   #main user interface to choose action
    option = True 
    clear_screen()
    print("OPTIONS MENU: ")
    print("=================")
    choice = lc.Storage.display_options(project_assignment) + 1
    clear_screen()

    # input new item. same method for all items
    choice_check = pick_options(choice, [1, 2], ["customer", "book"])
    if choice_check[0]:
        item = choice_check[1]
        while option:  
            clear_screen() 
            print(f"ADD A NEW {item.upper()}", "\n")
            item_data.new_item(item)
            option = end_check(f"Would you like to add another {item}?")
    
    
    # loan or return a book. Both are the same transaction with opposite directionality
    # 3(loan) -> dest = customer, 4(return) -> dest = library
    choice_check = pick_options(choice, [3, 4], ["book", "book"])
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
            option = end_check(f"Would you like to add another {item}?")
    
    # Display item (works for both book or cutomer depending on choice)
    choice_check = pick_options(choice, [5, 6], ["book", "customer"])
    if choice_check[0]:
        while option:
            print(f"DISPLAYING ALL {choice_check[1].upper()}S: ")
            x = item_data.get_item() #choose total item list file
            y = item_data.display_list(x, choice_check[1], "", "print")   
            option = end_check()
                
    # display loan list. all or only overdue -> depends on choice
    choice_check = pick_options(choice, [7, 8], ["", ""])
    if choice_check[0]:
        while option:
            overdue = False #default is full list
            print(f"{project_assignment[choice - 1].upper()}: ")
            if choice == 8:
                overdue = True #only overdue loans
            storage.item_stock(overdue)
            option = end_check()
                
    #find any item. Item type depends on choice.
    #item Id chosen will remain in "search_memory"
    choice_check = pick_options(choice, [9, 10], ["book", "customer"])
    if choice_check[0]:
        while option:
            print(choice_check[1])
            print(f"FIND {choice_check[1].upper()} BY DETAIL")
            print("Search will allow partial detail (even 1 letter or digit will suffice)")
            search_memory = item_data.find_item(choice_check[1], True)
            if search_memory:
                search_memory = list(search_memory.keys())[0]
            x = input()
    
    #Delete items item type depends on choice
    #Item is not deleted but type is changed to "deleted" + old type
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
            
            option = end_check()  
            
            
    choice_check = pick_options(choice, [13], [" "])
    if choice_check[0]:
        x = input("Aborting program. Are you sure? (Y/N) ")
        y = input(f"{x.lower()}")
        if x.lower == "y":
            break
        




