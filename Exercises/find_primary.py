import time
primary_list = []
start_time = time.time()
for counter in range(2,1000):
    i = 2
    is_primary = True
    while i < counter:
        if counter % i:    
            # if the condition is true it means it is not dividable and we go to the next
            i += 1
        else:
            # if the condition is false it means it is divadable so we stop the loop
            is_primary = False
            i = counter
    if is_primary:
        primary_list.append(counter)
end_time = time.time()
run_time = end_time - start_time
print(primary_list)
print("run time:", run_time)