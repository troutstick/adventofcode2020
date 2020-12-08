import glob
import time
import sys
import os


def block_print():
    sys.stdout = open(os.devnull, 'w')

def enable_print():
    sys.stdout = sys.__stdout__

files = [(f, open(f).read()) for f in glob.glob('day?.py')]
for f_name, f in files:
    block_print()
    start = time.perf_counter()
    exec(f)
    stop = time.perf_counter()
    enable_print()
    print(f"The time to execute {f_name} was {stop-start:0.4f} seconds")
