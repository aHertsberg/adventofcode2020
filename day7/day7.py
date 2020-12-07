import re


def get_bags(bags, bag_type, money_bag):
    contains = bags[bag_type]
    contains_money_bag = False
    if bag_type == money_bag:
        # This implies that the shiny gold bag contains itself -1 in the end will work
        contains_money_bag = True 
    elif not contains:
        contains_money_bag = False
    else:
        for count, bag in contains:
            if get_bags(bags, bag, money_bag):
                contains_money_bag = True
    return contains_money_bag


with open("input.txt", "r") as f:
    lines = f.readlines()

bags = {}
for line in lines:
    line = line.rstrip()
    entry = line.replace(' contain', ',').split(', ')
    key = entry[0][:-5]
    contains = entry[1:]
    if not key in bags.keys():
        bags[key] = []
    for bag in contains:
        if bag == 'no other bags.':
            break
        split = bag.split(' ') # How to name variables 101
        n = int(split[0])
        bag_kind = ' '.join(split[1:-1])
        bags[key].append((n, bag_kind))

print(bags)
count = 0
for bag_type in bags.keys():
    print(bag_type)
    if get_bags(bags, bag_type, 'shiny gold'):
        count += 1
print(count - 1)