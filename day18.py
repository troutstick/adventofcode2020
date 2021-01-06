from collections import defaultdict
from functools import reduce
from operator import add, mul
from typing import DefaultDict, List

def remove_whitespace(string):
    return ''.join(string.split())

with open('inputs/day18.txt', 'r') as f:
    instructions = [list(remove_whitespace(s)) for s in f]

def parens(expr):
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



def operator(l_expr, r_expr):
    pass

match_char = defaultdict(lambda: int)
match_char.update({
    '(' : parens,
    '*' : mul,
    '+' : add
})

# print(int('10'))

# a = match_char['h']
# print(a('10'))



def eval(expr, prev=0):
    print(f"prev is {prev}, expr is {expr}")
    if not expr:
        return prev
    c = expr[0]
    if type(c) is list:
        return eval(c)
    elif c == '(':
        expr = parens(expr[1:])
        print(f"the parens expr is {expr}")
        return eval(eval(expr[1:]), prev=eval(expr[0]))
    elif c == '*':
        print(f"returning {prev} times {expr[1:]}")
        prev *= int(expr[1])
        return eval(expr[2:], prev)
    elif c == '+':
        print(f"returning {prev} plus {expr[1:]}")
        prev += int(expr[1])
        return eval(expr[2:], prev)
    else:
        # print(f"trying to evaluate {expr}")
        return eval(expr[1:], int(c))


def find_parens(expr):
    stack = []
    parens = {}
    for i in range(len(expr)):
        if expr[i] == '(':
            stack.append(i)
        elif expr[i] == ')':
            parens[stack.pop()] = i
    return parens

operators = {'*':mul,'+':add}

def parse(expr):
    stack = []
    rpn = []
    for c in expr:
        try:
            rpn.append(int(c))
        except ValueError:
            if c == '(':
                stack.append(c)
            elif c in operators:
                while stack and stack[-1] in operators:
                    rpn.append(stack.pop())
                stack.append(c)
            else:
                # c is ')'
                stack_top = stack.pop()
                while stack_top != '(':
                    rpn.append(stack_top)
                    stack_top = stack.pop()
    while stack:
        rpn.append(stack.pop())
    return rpn

def eval2(rpn):
    stack = []
    for c in rpn:
        if c in operators:
            stack.append(operators[c](stack.pop(), stack.pop()))
        else:
            stack.append(c)
    return stack[0]


# test_str = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
# print(test_str)
# test_rpn = parse(remove_whitespace(test_str))
# print(test_rpn)
# print(eval2(test_rpn))
# print(test)
# print(test[0])
# print(test_str)
# print(f"evaled as {eval(list(remove_whitespace(test_str)))}")

print(f"The answer to part 1 is {reduce(add, map(eval2, map(parse, instructions)))}")
