import regex as re

def parse_rule(rule):
    if rule[0] == '"':
        return rule[1] # for matching char
    else:
        return [[int(i) for i in clause.split()] for clause in rule.split('|')]

def re_pattern(num=0, recursive=False):
    if recursive and num == 0:
        return f"({re_pattern(42, recursive)})+(?<x>{re_pattern(42, recursive)}(?&x)?{re_pattern(31, recursive)})"
    elif num == 0:
        return f"({re_pattern(42)})({re_pattern(42)})({re_pattern(31)})$"

    rule = rules[num]
    if type(rule) is list:
        s = ''
        for clause in rule:
            for i in clause:
                s += f"({re_pattern(i, recursive)})"
            s += '|'
        return s[:-1] # discard final or
    else:
        return rule

with open('inputs/day19test.txt', 'r') as f:
    rules, messages = f.read().split('\n\n')
    rules = {int(i):parse_rule(rule) 
        for i, rule in [r.split(': ') for r in rules.splitlines()]}
    messages = messages.split()
# print(rules)
# print(messages)
print(re_pattern(0, True))

p = re.compile(f"^({re_pattern()})$")
print(f"The answer to part 1 is {sum(map(lambda s: bool(p.match(s)), messages))}")

p = re.compile(re_pattern(recursive=True))
# for m in messages:
#     if p.match(m):
#         print(m)
# above 270
print(f"The answer to part 2 is {sum(map(lambda s: bool(p.match(s)), messages))}")
