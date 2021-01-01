from functools import reduce
from operator import add

with open('inputs/day17.txt', 'r') as f:
    lines = [line.strip() for line in f]

def neighbor_set(coord):
    neighbors = set()
    X, Y, Z = coord
    for x in range(X-1, X+2):
        for y in range(Y-1, Y+2):
            for z in range(Z-1, Z+2):
                n = (x, y, z)
                if n != coord:
                    neighbors.add(n)
    return neighbors

active = set()
for x in range(len(lines)):
    for y in range(len(lines[0])):
        # if active
        if lines[x][y] == '#':
            active.add((x,y,0))

for _ in range(6):
    next_active = set()

    all_neighbor_sets = [neighbor_set(pos) for pos in active]
    all_neighbors = reduce(set.union, all_neighbor_sets)

    for pos, pos_neighbors in zip(active, all_neighbor_sets):
        num_active_neighbors = reduce(
            add, 
            map(lambda p: p in active, pos_neighbors)
        )
        if num_active_neighbors in range(2,4):
            next_active.add(pos)

    for pos in all_neighbors:
        num_active_neighbors = reduce(
            add,
            map(lambda p: p in active, neighbor_set(pos))
        )
        if num_active_neighbors == 3:
            next_active.add(pos)
    active = next_active

print(f"The answer to part 1 is {len(active)}")