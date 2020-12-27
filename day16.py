import re
from typing import Generator

def process_fields(string):
    s = set()
    p = re.compile('[\d]+-[\d]+ or [\d]+-[\d]+')
    ranges = p.findall(string)
    p = re.compile('[\d]+')
    for r in ranges:
        a,b,c,d = [int(i) for i in p.findall(r)]
        f = lambda x: (x >= a and x <= b) or (x >= c and x <= d)
        s.add(f)
    return s


with open('inputs/day16test.txt') as f:
    instructions = f.read().split('\n\n')
    p = re.compile('[\d]+')
    nearby_vals = [int(i) for i in p.findall(instructions[2])]
    field_set = process_fields(instructions[0])

def in_no_fields(i):
    for f in field_set:
        if f(i):
            print(f"{i} has a field")
            return False
    print(f"{i} is fieldless")
    return True

error_rate = sum(filter(in_no_fields, nearby_vals))
print(f"The answer to part 1 is {error_rate}")
