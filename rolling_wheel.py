import time
import os
WHEEL = "-\|/-\|/"
os.system('cls||clear')
for c in range(250):
    print(WHEEL[c % len(WHEEL)], end='\r')
    # https://stackoverflow.com/a/36941376/3413574
    # os.system('cls||clear')
    time.sleep(0.1) ####tHIS IS BETTER..
