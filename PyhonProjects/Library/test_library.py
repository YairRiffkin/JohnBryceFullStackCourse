import LibraryClass as lc
import random
import pytest

item_to_test = "book"
item_list = lc.DataItem()
list_of_items = item_list.get_item()


@pytest.fixture
def start_fixture():
    item_list = lc.DataItem()
    list_of_items = item_list.get_item()
    return list_of_items

@pytest.fixture
def book_item_fixture(start_fixture):
    test_list = []
    for index in start_fixture:
        if start_fixture[index]["type"] == "book":
            test_list.append(index)
    length = len(test_list)
    x = random.randrange(0, length) 
    chosen_item = test_list[x]
    return start_fixture[chosen_item]

@pytest.fixture
def customer_item_fixture(start_fixture):
    test_list = []
    for index in start_fixture:
        if start_fixture[index]["type"] == "customer":
            test_list.append(index)
    length = len(test_list)
    x = random.randrange(0, length) 
    chosen_item = test_list[x]
    return start_fixture[chosen_item]

def test_compare_book(book_item_fixture):
    item_list = lc.DataItem()
    assert item_list.compare(book_item_fixture)[0] == True
            
def test_compare_customer(customer_item_fixture):
    item_list = lc.DataItem()
    assert item_list.compare(customer_item_fixture)[0] == True        
      


