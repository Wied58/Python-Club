#!/anaconda3/bin/python
from datetime import datetime

import random
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
	21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
	41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range (10):
    print ("We've looped this many times: ", i)    
    right_this_minute = datetime.today().minute
    print("right_this_minute = ",right_this_minute)
    if right_this_minute in odds:
    	print("This minute seems a little odd.")
    else:
            print("Not an odd minute")
    wait_time = random.randint(1, 15)
    print ("Wait_time = ",wait_time)
    time.sleep(wait_time)


# end of range loop


