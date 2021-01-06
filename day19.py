with open('inputs/day19.txt', 'r') as f:
    rules, messages = f.read().split('\n\n')
    rules = [r for r in rules.splitlines()]
    messages = [m for m in messages.split()]
print(rules)
print(messages)