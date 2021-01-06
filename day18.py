from functools import reduce
from operator import add, mul

ops = {'*':mul,'+':add}

def parse(add_before_mul):
    def left_has_precedence(l_op, r_op):
        return (not add_before_mul) or (l_op == '+' and r_op == '*')

    def shunting_yard(expr):
        stack, rpn = [], []
        for c in expr:
            try:
                rpn.append(int(c))
            except ValueError:
                if c == '(':
                    stack.append(c)
                elif c in ops:
                    while stack and stack[-1] in ops and left_has_precedence(stack[-1], c):
                        rpn.append(stack.pop())
                    stack.append(c)
                else: # c is ')'
                    stack_top = stack.pop()
                    while stack_top != '(':
                        rpn.append(stack_top)
                        stack_top = stack.pop() # discard '('
        stack.reverse()
        rpn.extend(stack)
        return rpn
    
    return shunting_yard

def eval(rpn):
    rpn_operate = lambda stack, c: stack + [ops[c](stack.pop(), stack.pop()) if c in ops else c]
    return reduce(rpn_operate, rpn, [])[0]

def remove_whitespace(string):
    return ''.join(string.split())

with open('inputs/day18.txt', 'r') as f:
    instructions = [list(remove_whitespace(s)) for s in f]

print(f"The answer to part 1 is {reduce(add, map(eval, map(parse(False), instructions)))}")
print(f"The answer to part 2 is {reduce(add, map(eval, map(parse(True), instructions)))}")
