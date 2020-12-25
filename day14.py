import re

with open('inputs/day14.txt') as f:
    memory = {}
    instructions = [line.strip().split('=') for line in f]
    line: str
    on_mask = 0
    off_mask = 0
    for var, value in instructions:
        if re.match('^mask', var):
            on_mask = int(value.replace('X', '0'), 2)
            off_mask = int(value.replace('X', '1'), 2)
        else:
            pattern = re.compile('[0-9]+')
            address = int(pattern.search(var).group())
            to_write = int(value)
            to_write |= on_mask
            to_write &= off_mask
            memory[address] = to_write
    print(f"The answer to part 1 is {sum(memory.values())}")

    for var, value in instructions:
        if re.match('^mask', var):
            on_mask = int(value.replace('X', '0'), 2)
        else:
            reverse = value[::-1]
            pattern = re.compile('[0-9]+')
            address = int(pattern.search(var).group()) | on_mask
            for i in range(36):
                if reverse[i] == 'X':
                    