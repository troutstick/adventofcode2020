from functools import reduce
from operator import add

def remove_whitespace(string):
    return ''.join(string.split())

with open('inputs/day18.txt', 'r') as f:
    instructions = [remove_whitespace(s) for s in f]

def parens(expr: list[str]) -> list[list[str], list[str]]:
    # split expr into before/after parens
    i = 0
    while i < len(expr):
        c = expr[i]
        if c == '(':
            expr[i:] = parens(expr[i+1:])
        elif c == ')':
            return [expr[:i]] + expr[i+1:]
        i += 1
    raise Exception("invalid string given")


print(parens([c for c in remove_whitespace(
    "(2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")]))

def operator(l_expr, r_expr):
    pass

def compute_line(expr):
    for i in range(len(expr)):
        match_char[expr[i]](expr[i+1:])
    pass

match_char = {
    '(' : parens,
}

print(f"The answer to part 1 is {reduce(add, map(compute_line, instructions))}")