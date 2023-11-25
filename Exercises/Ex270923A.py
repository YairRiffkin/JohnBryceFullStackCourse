import datetime
import time

while True:    
    x = datetime.datetime.now()
    print(x.strftime("%X"))
    time.sleep(1)