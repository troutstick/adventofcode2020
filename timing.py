import glob
import time
import sys
import os

def block_print():
    sys.stdout = open(os.devnull, 'w')

def enable_print():
    sys.stdout = sys.__stdout__

total_time = 0

files = [(f, open(f).read()) for f in glob.glob('day?.py')]

for f_name, f in files:
    block_print()
    start = time.perf_counter()
    exec(f)
    stop = time.perf_counter()
    enable_print()

    exec_time = stop - start
    total_time += exec_time
    print(f"The time to execute {f_name} was {exec_time:0.4f} seconds")

print(f"The total time to execute was {total_time:0.4f} seconds")
