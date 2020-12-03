with open('inputs/day3.txt', 'r') as file:
    lines = [line for line in file]
    line_len = len(lines[0]) - 1

    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]

    answer = 1
    for right, down in slopes:
        pos = 0
        tree_cnt = 0
        for i in range(0, len(lines), down):
            line = lines[i]
            if line[pos] == '#':
                tree_cnt += 1
            pos = (pos + right) % line_len
        print(f"Encountered {tree_cnt} trees for a slope of {right} right, {down} down")
        answer *= tree_cnt
    print(f"The answer for part 2 is {answer}")