import re

def parse_rule(rule):
    if rule[0] == '"':
        return rule[1] # for matching char
    else:
        return [[int(i) for i in clause.split()] for clause in rule.split('|')]

def re_pattern(num=0):
    rule = rules[num]
    if type(rule) is list:
        s = ''
        for clause in rule:
            for i in clause:
                s += f"({re_pattern(i)})"
            s += '|'
        return s
    else:
        return rule

with open('inputs/day19.txt', 'r') as f:
    rules, messages = f.read().split('\n\n')
    rules = {int(i):parse_rule(rule) 
        for i, rule in [r.split(': ') for r in rules.splitlines()]}
    messages = messages.split()
# print(rules)
# print(messages)

p = re.compile(f"^({re_pattern()})$")
print(f"The answer to part 1 is {sum(map(lambda s: bool(p.match(s)), messages))}")
