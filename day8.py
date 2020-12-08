pointer = 0
accumulator = 0

def nop(num):
    global pointer
    pointer += 1

def acc(num):
    global pointer
    global accumulator
    pointer += 1
    accumulator += num

def jmp(num):
    global pointer
    pointer += num

func_map = {
    'jmp' : jmp,
    'nop' : nop,
    'acc' : acc
}

def execute(instructions):
    global pointer
    global accumulator
    inf_loop = True
    visited = set()
    while pointer not in visited:
        visited.add(pointer)
        operator, arg = instructions[pointer]
        func_map[operator](int(arg))
        if pointer == len(instructions):
            inf_loop = False
            break
    rv = accumulator
    pointer = 0
    accumulator = 0
    return rv, inf_loop

def fix_program(program, orig, new):
    for num in filter(lambda i: program[i][0] == orig, range(len(program))):
        new_program = [list(i) for i in program]
        new_program[num][0] = new
        acc_val, inf_loop = execute(new_program)
        if not inf_loop:
            print(f"The fixed program exited with value {acc_val}")

with open('inputs/day8.txt','r') as file:
    program = [line.split() for line in file]
    print(f"The accumulator reaches {execute(program)[0]} before looping")
    fix_program(program, 'jmp', 'nop')
    fix_program(program, 'nop', 'jmp')
