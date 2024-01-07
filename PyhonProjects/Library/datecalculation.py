import json
import LibraryClass as lc
import os
import time
from pprint import pprint
from tabulate import tabulate
import datetime
item = lc.DataItem()
stor = lc.Storage()

x = stor.last_transaction("000001", "000025", "output")
print(x)
y = datetime.datetime.now()
date_format = "%d-%m-%Y %X"
result = datetime.datetime.strptime(x, date_format)
time_passed = y - result
print(int(time_passed.days))