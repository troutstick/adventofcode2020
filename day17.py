from functools import reduce
from operator import add

def neighbor_set_3d(coord):
    X, Y, Z = coord
    return set(filter(
                lambda n: n != coord, 
                [(x,y,z)
                for x in range(X-1, X+2) 
                for y in range(Y-1, Y+2) 
                for z in range(Z-1, Z+2)]
            )
        )

def neighbor_set_4d(coord):
    X, Y, Z, W = coord
    return set(filter(
                lambda n: n != coord, 
                [(x,y,z,w)
                for x in range(X-1, X+2) 
                for y in range(Y-1, Y+2) 
                for z in range(Z-1, Z+2) 
                for w in range(W-1, W+2)]
            )
        )

def solve(active, neighbor_set):
    for _ in range(6):
        neighbors = {pos:neighbor_set(pos) for pos in active}
        neighbors_of_active = reduce(set.union, neighbors.values())
        neighbors.update({pos:neighbor_set(pos) for pos in neighbors_of_active})

        def next_state(candidates, activate_func):
            num_active_neighbors = lambda pos: reduce(add, map(lambda p: p in active, neighbors[pos]))
            has_enough_neighbors = lambda pos: activate_func(num_active_neighbors(pos))
            return set(filter(has_enough_neighbors, candidates))

        active = next_state(active, lambda n: n == 2 or n == 3).union(next_state(neighbors_of_active, lambda n: n == 3))

    return len(active)

with open('inputs/day17.txt', 'r') as f:
    lines = [line.strip() for line in f]
    starter_coords = [(x,y,0) for x in range(len(lines)) for y in range(len(lines[0]))]
    starter_4d = [(x,y,z,0) for x, y, z in starter_coords]
    is_active = lambda n: lines[n[0]][n[1]] == '#'
    print(f"The answer to part 1 is {solve(set(filter(is_active, starter_coords)), neighbor_set_3d)}")
    print(f"The answer to part 2 is {solve(set(filter(is_active, starter_4d)), neighbor_set_4d)}")
