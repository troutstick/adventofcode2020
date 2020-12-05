def to_bin(string, zero_char, one_char):
    string = string.replace(zero_char, '0')
    string = string.replace(one_char, '1')
    return int(string, 2)

with open('inputs/day5.txt', 'r') as file:
    high = 0
    seats = set()
    for line in file:
        line = line.strip()
        row = to_bin(line[:7], 'F', 'B')
        col = to_bin(line[-3:], 'L', 'R')
        seat_num = (row * 8) + col
        seats.add(seat_num)
        high = max(high, seat_num)
    
    print(high)
    prev_i = 0.5
    for i in seats:
        if i - prev_i == 2:
            print(i-1)
        prev_i = i