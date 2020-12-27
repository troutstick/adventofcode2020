import re

p = re.compile('[\d]+')

def process_fields(string: str):
    D = {}
    fields = [s.split(':') for s in string.splitlines()]

    # p = re.compile('[\d]+-[\d]+ or [\d]+-[\d]+')
    # ranges = p.findall(string)
    for name, r in fields:
        a,b,c,d = [int(i) for i in p.findall(r)]

        def f(x, a=a, b=b, c=c, d=d): 
            return (x >= a and x <= b) or (x >= c and x <= d)
        
        D[f] = name
    return D


with open('inputs/day16.txt') as f:
    ins = f.read().split('\n\n')
    tickets = [[int(i) for i in p.findall(line)] for line in ins[2].splitlines()]
    flat_tickets = [item for sublist in tickets for item in sublist]
    field_dict = process_fields(ins[0])

def in_no_fields(i):
    for f in field_dict:
        if f(i):
            return False
    return True

def valid_ticket(t):
    for i in t:
        if in_no_fields(i):
            return False
    return True

error_rate = sum(filter(in_no_fields, flat_tickets))
print(f"The answer to part 1 is {error_rate}")

valid_tickets = [t for t in filter(valid_ticket, tickets)]
for f, name in field_dict.items():
    