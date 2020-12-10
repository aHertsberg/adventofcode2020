with open("input.txt", "r") as f:
    lines = f.readlines()

joltages = list(map(int, lines))
joltages.sort()
joltages.insert(0, 0)  # add socket joltage
joltages.append(joltages[-1] + 3)  # add the end device
difs = []
for i in range(len(joltages) - 1):
    difs.append(joltages[i + 1] - joltages[i])

# this could've been made to a dict or list or something
one_joltage = difs.count(1)
two_joltages = difs.count(2)
three_joltages = difs.count(3)

print(
    "The number of 1-jolt differences multiplied by the number of 3-jolt differences is {}".format(
        one_joltage * three_joltages
    )
)


def evaluate_segment(segment, evaluated=[]):
    if len(segment) == 1:
        return 1
    difs = []
    permutations = 0
    for i in range(len(segment) - 1):
        difs.append(segment[i + 1] - segment[i])
    if max(difs) > 3:
        return 0
    else:
        permutations += 1
        evaluated.append(segment)
        # first and last item in segment needs to stay the same
        for joltage in segment[1:-1]:
            new_segment = segment.copy()
            new_segment.remove(joltage)
            if not new_segment in evaluated:
                permutations += evaluate_segment(new_segment, evaluated)
    return permutations


segments = []
previous = 0
for i, dif in enumerate(difs):
    if dif == 3:
        segments.append(joltages[previous : i + 1])
        previous = i + 1

permutations = 1
for segment in segments:
    permutations *= evaluate_segment(segment)

print(permutations)

# Now that I think about things, since there are only 1 or 3 joltage steps,
# the permutations are only a function of the segment length. This could be
# used for a solution with _these_ adapters, but not really for a "global"
# solution
