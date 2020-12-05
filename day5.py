def to_bin(string, zero_char, one_char):
    string = string.replace(zero_char, '0')
    string = string.replace(one_char, '1')
    return int(string, 2)

with open('inputs/day5.txt', 'r') as file:
    high = 0
    seats = set()
    for line in file:
        row = to_bin(line[:7], 'F', 'B')
        col = to_bin(line[-4:], 'L', 'R') # account for \n
        seats.add((row * 8) + col)
    
    print(f"The largest seat number is {max(seats)}")

    prev_i = 0
    for i in seats:
        if i - prev_i == 2:
            print(f"Your seat number is {i-1}")
            break
        prev_i = i
