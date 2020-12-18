from enum import IntEnum

class Dir(IntEnum):
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3

x = 0
y = 0
curr_dir = Dir.EAST

def north(i):
    global y
    y += i

def south(i):
    global y
    y -= i

def east(i):
    global x
    x += i

def west(i):
    global x
    x -= i

def left(i):
    global curr_dir
    curr_dir = (curr_dir - (i // 90)) % 4

def right(i):
    global curr_dir
    curr_dir = (curr_dir + (i // 90)) % 4

forward_map = {
    Dir.NORTH : north,
    Dir.SOUTH : south,
    Dir.EAST  : east,
    Dir.WEST  : west,
}

def forward(i, waypoint_mode_on):
    forward_map[curr_dir](i)

action_map = {
    'N' : north,
    'S' : south,
    'E' : east,
    'W' : west,
    'L' : left,
    'R' : right,
    'F' : forward
}

with open('inputs/day12.txt', 'r') as f:
    directions = [(s[0], int(s[1:])) for s in [line.strip() for line in f]]
    for action, dist in directions:
        action_map[action](dist)
    print(f"Part 1: Traveled a distance of {abs(x)+abs(y)}")