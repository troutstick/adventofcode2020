import re

parent_to_children = {}

def can_contain_gold(bag):
    if bag == 'shiny gold':
        return True

    for children in parent_to_children[bag]:
        if can_contain_gold(children[0]):
            return True
    return False

def count_num_bags(bag):
    children = parent_to_children[bag]
    num_bags = 0
    for child, num_child in children:
        num_bags += num_child
        num_bags += num_child * count_num_bags(child)
    return num_bags

with open('inputs/day7.txt','r') as file:
    for line in file:
        line = re.sub('bags*', '', line) # remove bags from str
        strings = line.split('contain')
        parent = strings[0].strip()
        children_list = [
            s.strip() for s in filter(
                lambda a: a != '', 
                re.split('[,\.]', strings[1].strip())
            )
        ]
        children = set()
        num_bags = 0
        for child in children_list:
            if child == 'no other':
                break
            num_child = int(re.match('\d+', child)[0])
            num_bags += num_child
            child = re.sub('\d+', '', child).strip()
            children.add((child, num_child))
        parent_to_children[parent] = children
    
    num_bags_with_gold = 0
    for parent in parent_to_children.keys():
        if can_contain_gold(parent) and parent != 'shiny gold':
            num_bags_with_gold += 1

    print(f"The answer to part 1 is {num_bags_with_gold}")
    print(f"The answer to part 2 is {count_num_bags('shiny gold')}")
