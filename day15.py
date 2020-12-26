def solve(in_list, length):
    last_turn = len(in_list) + 1  # account for start
    prev = {i: turn for i, turn in zip(in_list, range(1, last_turn))}
    last_spoken = 0
    while last_turn < length:
        if last_spoken in prev.keys():
            prev_seen_turn = prev[last_spoken]
            prev[last_spoken] = last_turn
            last_spoken = last_turn - prev_seen_turn
        else:
            prev[last_spoken] = last_turn
            last_spoken = 0
        last_turn += 1
    return last_spoken

with open('inputs/day15.txt') as f:
    in_list = [int(c) for c in f.read().split(',')]
    print(f"The answer to part 1 is {solve(in_list, 2020)}")
    print(f"The answer to part 2 is {solve(in_list, 30000000)}")
