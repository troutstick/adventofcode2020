with open('inputs/day16.txt') as f:
    instructions = f.read().split('\n\n')
    for i in instructions:
        print(i)
        print()
    instructions[0] = [instructions[0].split()]
    print(len(instructions))