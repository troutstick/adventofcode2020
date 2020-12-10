cnt_dict = {}

def count_perms(jolts):
    # extremely crude memoizing agh
    if len(jolts) == 1:
        cnt_dict[jolts[0]] = 1
        return 1
    count=0
    for i in range(1,min(4, len(jolts))):
        diff = jolts[i] - jolts[0]
        if diff > 3:
            break
        if jolts[i] in cnt_dict:
            count += cnt_dict[jolts[i]]
        else:
            cnt_dict[jolts[i]] = count_perms(jolts[i:])
            count += cnt_dict[jolts[i]]
    cnt_dict[jolts[0]] = count
    return count

with open('inputs/day10.txt', 'r') as file:
    jolts = [int(s) for s in file]
    jolts.sort()
    jolts.append(max(jolts) + 3)
    curr_joltage = 0

    diffs = {i : 0 for i in range(1,4)}

    prev_j = 0
    for j in jolts:
        diff = j - prev_j
        diffs[diff] += 1
        prev_j = j
    
    print(f"Answer to part 1 is {diffs[1] * diffs[3]}")

    jolts.insert(0, 0) # first jolt counts towards perms
    print(f"Answer to part 2 is {count_perms(jolts)}")
