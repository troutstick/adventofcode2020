from enum import IntEnum

class Dir(IntEnum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3

def solve(directions, is_part_1):
    if is_part_1:
        x = 0
        y = 0
    else:
        x = 10
        y = 1

    curr_dir = Dir.EAST

    # for part 2
    curr_x = 0
    curr_y = 0

    # sin(degree)
    sin = {
        0   : 0,
        90  : 1,
        180 : 0,
        270 : -1
    }

    cos = {
        0   : 1,
        90  : 0,
        180 : -1,
        270 : 0
    }

    def rotate(degrees):
        if is_part_1:
            nonlocal curr_dir
            curr_dir = (curr_dir - (degrees // 90)) % 4
        else:
            nonlocal x, y
            degrees %= 360
            cosdeg = cos[degrees]
            sindeg = sin[degrees]
            print(f"cos: {cosdeg} sin: {sindeg}")
            new_x = x * cosdeg - y * sindeg
            new_y = x * sindeg - y * cosdeg
            x, y = new_x, new_y
        
    def north(i):
        nonlocal y
        y += i

    def south(i):
        nonlocal y
        y -= i

    def east(i):
        nonlocal x
        x += i

    def west(i):
        nonlocal x
        x -= i

    def left(i):
        rotate(i)

    def right(i):
        rotate(-i)

    forward_map = {
        Dir.NORTH : north,
        Dir.SOUTH : south,
        Dir.EAST  : east,
        Dir.WEST  : west,
    }

    def forward(i):
        if is_part_1:
            forward_map[curr_dir](i)
        else:
            nonlocal curr_x, curr_y
            curr_x += x * i
            curr_y += y * i

    action_map = {
        'N' : north,
        'S' : south,
        'E' : east,
        'W' : west,
        'L' : left,
        'R' : right,
        'F' : forward
    }
    
    for action, dist in directions:
        action_map[action](dist)
        if not is_part_1:
            print(f"action is {action}, dist is {dist}")
            print(f"ship is at {curr_x, curr_y}")
            print(f"waypoint is {x, y}")
            print()

    if is_part_1:
        curr_x, curr_y = x, y

    return abs(curr_x) + abs(curr_y)


with open('inputs/day12.txt', 'r') as f:
    directions = [(s[0], int(s[1:])) for s in [line.strip() for line in f]]
    print(f"Part 1: Traveled a distance of {solve(directions, True)}")
    print(f"Part 2: Traveled a distance of {solve(directions, False)}")