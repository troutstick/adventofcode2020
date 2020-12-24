from functools import reduce
import operator as op

def crt(div_to_modulus, M):
    t = 0
    for a, m in div_to_modulus:
        M_div_m = M // m
        b = M_div_m * pow(M_div_m, -1, m)  # inverse mod
        t = (t + (a * b)) % M
    return t
    
with open('inputs/day13.txt', 'r') as f:
    depart_time = int(f.__next__())
    buses = [x.strip() for x in f.__next__().split(',')]
    buses_in_service = [int(i) for i in filter(lambda c: c != 'x', buses)]
    wait_times = {(b - depart_time % b) : b for b in buses_in_service}
    min_time = min(wait_times)
    print(f"The answer to part 1 is {min_time * wait_times[min_time]}")

    div_to_modulus = [(-i, int(buses[i])) for i in range(len(buses)) if buses[i] != 'x']
    M = reduce(op.mul, buses_in_service)

    print(f"The answer to part 2 is {crt(div_to_modulus, M)}")
