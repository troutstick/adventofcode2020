with open("inputs/day2.txt", "r") as file:
    part_1 = 0
    part_2 = 0
    for line in file:
        L = line.split(':')
        pw = L[1].strip()
        L = L[0].split()
        char = L[1].strip()
        L = L[0].split('-')
        low = int(L[0])
        high = int(L[1])
        char_num = pw.count(char)
        if char_num >= low and char_num <= high:
            part_1 += 1
        if (pw[low-1] == char) ^ (pw[high-1] == char):
            part_2 += 1
    print(part_1)
    print(part_2)