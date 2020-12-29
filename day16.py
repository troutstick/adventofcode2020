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
    return D, len(fields)


with open('inputs/day16.txt') as f:
    ins = f.read().split('\n\n')
    tickets = [[int(i) for i in p.findall(line)] for line in ins[2].splitlines()]
    flat_tickets = [item for sublist in tickets for item in sublist]
    field_dict, num_fields = process_fields(ins[0])

def in_no_fields(i):
    for f in field_dict:
        if f(i):
            return False
    return True

def is_valid_ticket(t):
    for i in t:
        if in_no_fields(i):
            return False
    return True

def single_true(iterable):
    i = iter(iterable)
    return any(i) and not any(i)

error_rate = sum(filter(in_no_fields, flat_tickets))
print(f"The answer to part 1 is {error_rate}")

field_to_index = {}
valid_tickets = [t for t in filter(is_valid_ticket, tickets)]

for in_range, field_name in field_dict.items():

    def is_valid_index(i): 
        return all(map(lambda t: in_range(t[i]), valid_tickets))
    
    if single_true(map(is_valid_index, range(num_fields))):
        t = valid_tickets[0]
        for i in range(num_fields):
            if in_range(t[i]):
                field_to_index[field_name] = i
                break
        break