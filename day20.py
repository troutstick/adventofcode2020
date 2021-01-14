def horizontal_flip(sq):
    return [s[::-1] for s in sq]

def vertical_flip(sq):
    return sq[::-1]

def rotate(sq):
    return [''.join(row[i] for row in reversed(sq)) for i in range(len(sq))]
        
def print_sq(sq):
    print()
    for s in sq:
        print(s)

def is_neighbor(sq1, sq2):
    pass

with open('inputs/day20.txt', 'r') as f:
    squares = {int(num[-4:]): sq.strip().splitlines()
            for num, sq in [s.split(':') 
            for s in f.read().split('\n\n')]}

####
####
####
####

    neighbors = {}
    for i, sq1 in squares.items():
        print_sq(sq1)
        # print_sq(horizontal_flip(sq1))
        # print_sq(vertical_flip(sq1))
        print_sq(rotate(sq1))
        break
        neighbor_list = []
        for j, sq2 in squares.items():
            if i == j:
                continue
            elif is_neighbor(sq1, sq2):
                neighbor_list.append(sq2)
