def count_adjacent(state, row, col):
    count = 0
    for i in range(max(row-1, 0), min(row+2, len(state))):
        for j in range(max(col-1, 0), min(col+2, len(state[0]))):
            if not (i == row and j == col):
                if state[i][j] == '#':
                    count += 1
    return count

def count_far(state, row, col):
    def in_bounds(r,c):
        return r >= 0 and c >= 0 and r < len(state) and c < len(state[0])

    increments = [-1,0,1]
    count = 0
    for i in increments:
        for j in increments:
            if i or j:
                x = row + i
                y = col + j
                while in_bounds(x,y):
                    if state[x][y] == '.':
                        x += i
                        y += j
                    elif state[x][y] == '#':
                        count += 1
                        break
                    else:
                        break
    return count

def game(state, count_func, threshold):
    while True:
        next_state = [list(s) for s in state]
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == '#' and count_func(state, i, j) >= threshold:
                        next_state[i][j] = 'L'
                elif state[i][j] == 'L' and count_func(state, i, j) == 0:
                        next_state[i][j] = '#'

        if set(map(tuple, state)) == set(map(tuple, next_state)): # break if stable
            break
        state = next_state

    return sum([1 for sublist in state for i in sublist if i == '#']) # count num occupied

with open('inputs/day11.txt', 'r') as file:
    state = [[char for char in line.strip()] for line in file]
    print(f"The answer to part 1 is {game(state, count_adjacent, 4)}")
    print(f"The answer to part 2 is {game(state, count_far, 5)}")
