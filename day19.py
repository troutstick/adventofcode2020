def parse_rule(rule):
    if rule[0] == '"':
        return rule[1] # for matching char
    else:
        return [[int(i) for i in clause.split()] for clause in rule.split('|')]

with open('inputs/day19.txt', 'r') as f:
    rules, messages = f.read().split('\n\n')
    rules = {int(i):parse_rule(rule) 
        for i, rule in [r.split(': ') for r in rules.splitlines()]}
    messages = messages.split()
# print(rules)
# print(messages)


# print(parse_rule('130 90 | 50 53'))

def match(string, num=0):
    # consume string
    rule = rules[num]
    if type(rule) is list:
        for clause in rule:
            str_copy = string[:]
            for i in clause:
                str_copy = match(str_copy, i)
    else:
        return string[1:] if string[:1] == rule else string
    pass
