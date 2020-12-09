with open("input.txt", "r") as f:
    lines = f.readlines()


def pair_exists(next, values):
    state = False
    for x in values:
        for y in values:
            if x + y == next and x != y:
                state = True
    return state


for i in range(len(lines)):
    lines[i] = int(lines[i].rstrip())
    if i >= 25:
        pair_state = pair_exists(lines[i], lines[i - 25 : i])
        if pair_state == False:
            terminating_value = lines[i]
            break


print(terminating_value)
lower = 0
upper = 1
segment_sum = sum(lines[lower:upper])
while segment_sum != terminating_value:
    if segment_sum < terminating_value:
        upper += 1
    else:
        lower += 1
    segment_sum = sum(lines[lower:upper])

segment = lines[lower:upper]
smallest = min(segment)
largest = max(segment)
print(smallest + largest)
