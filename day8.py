def execute(instructions):
    
    def nop(num):
        nonlocal pointer
        pointer += 1

    def acc(num):
        nonlocal pointer
        nonlocal accumulator
        pointer += 1
        accumulator += num

    def jmp(num):
        nonlocal pointer
        pointer += num

    decode_op = {
        'jmp' : jmp,
        'nop' : nop,
        'acc' : acc
    }

    pointer = 0
    accumulator = 0

    visited = set()
    while pointer not in visited:
        visited.add(pointer)
        op, arg = instructions[pointer]
        decode_op[op](int(arg))
        if pointer == len(instructions):
            return accumulator, False
    return accumulator, True

def fix_program(program, old_op, new_op):
    for num in filter(lambda i: program[i][0] == old_op, range(len(program))):
        new_program = [list(i) for i in program]
        new_program[num][0] = new_op
        exit_val, inf_loop = execute(new_program)
        if not inf_loop:
            print(f"The fixed program exited with value {exit_val}")
            break

with open('inputs/day8.txt','r') as file:
    program = [line.split() for line in file]
    print(f"The accumulator reaches {execute(program)[0]} before looping")
    fix_program(program, 'jmp', 'nop')
    fix_program(program, 'nop', 'jmp')
