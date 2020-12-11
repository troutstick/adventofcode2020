with open('inputs/day11.txt', 'r') as file:
    state = [[char for char in line.strip()] for line in file]

num_rows = len(state)
num_cols = len(state[0])

def count(state, row, col, count_far):
    in_bounds = lambda r,c: r >= 0 and c >= 0 and r < num_rows and c < num_cols
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i or j:
                x = row + i # so it doesn't count self
                y = col + j
                while in_bounds(x,y):
                    if count_far and state[x][y] == '.':
                        x += i
                        y += j
                    elif state[x][y] == '#':
                        count += 1
                        break
                    else:
                        break
    return count

def game(state, count_far, threshold):
    while True:
        next_state = [list(s) for s in state]
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == '#' and count(state, i, j, count_far) >= threshold:
                        next_state[i][j] = 'L'
                elif state[i][j] == 'L' and count(state, i, j, count_far) == 0:
                        next_state[i][j] = '#'

        if set(map(tuple, state)) == set(map(tuple, next_state)):
            break # break if stable
        state = next_state

    # count num occupied
    return len([i for sublist in state for i in sublist if i == '#']) 
    
print(f"The answer to part 1 is {game(state, False, 4)}")
print(f"The answer to part 2 is {game(state, True, 5)}")
