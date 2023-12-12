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

def pick_options(pick: any, choice= [], option= []):
    pick = int(pick)
    x = False
    y = []
    for i in zip(choice, option):
        if pick == i[0]:
            x = True
            y = i[1]
    return [x, y]
            
        
    
while True:   
    option = True 
    clear_screen()
    print("OPTIONS MENU: ")
    print("=================")
    choice = lc.Storage.display_options(project_assignment)
    clear_screen()

    choice_check = pick_options(choice[0], [1, 2], ["customer", "book"])
    if choice_check[0]:
        item = choice_check[1]
        while option:  
            clear_screen() 
            print(f"ADD A NEW {item.upper()}", "\n")
            item_data.new_item(item)
            x = input(f"Would you like to add another {item}? (Y/N) ")
            if x.lower() != "y":
                option = False
    
    choice_check = pick_options(choice[0], [3, 4], ["book", "book"])
    if choice_check[0]:
        while option: 
            print("[LOAN] or [RETURN] A BOOK")
            item = choice_check[1]
            print("Customer Details ==>")
            customer = item_data.find_item("customer", True)
            clear_screen()
            print("Book Details ==>")
            book = item_data.find_item("book", True)
            clear_screen()
            print(choice[1].upper())
            print(f"BOOK: {item_data.display_list(item, "", "print", book)}")
            print(f"CUSTOMER: {item_data.display_list("customer", "", "print", customer)}")
            x = input("Continue? (Y/N) ")
            if x.lower() == "y":
                if int(choice[0]) == 3:
                    source = "000001"
                    dest = customer
                if int(choice[0]) == 4:
                    source = customer
                    dest = "000001"
                item_value = item_data.get_item(book)
                value = float(item_value["value"])
                storage.transaction(book, source, dest, 1, value)
            x = input(f"Would you like to add another {item}? (Y/N)")
            if x.lower() != "y":
                option = False    
    choice_check = pick_options(choice[0], [5, 6], ["book", "customer"])
    if choice_check[0]:
        while option:
            print(f"DISPLAYING ALL {choice_check[1].upper()}S: ")   
            x = item_data.display_list(choice_check[1], "", "print")   
            x = input("Continue? (Y/N) ")
            if x.lower() != "n":
                option = False    
    




