from functools import reduce

with open('inputs/day6.txt', 'r') as file:
    groups = file.read().split('\n\n')
    num_anyone = 0
    num_everyone = 0
    for g in groups:
        p_sets = [set(s) for s in g.split()]
        S_anyone = reduce(set.intersection, p_sets)
        S_everyone = reduce(set.union, p_sets)
        num_anyone += len(S_anyone)
        num_everyone += len(S_everyone)
    print(f"The answer to part 1 is {num_everyone}")
    print(f"The answer to part 2 is {num_anyone}")
