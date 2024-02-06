#str = "Looping"
#for item in str:
#    print(item)

import time 
start_time = time.time()

for i in range(10):
    for j in range(150000):
        print(0, end = " ")
    print()

print(round((time.time()-start_time),2))