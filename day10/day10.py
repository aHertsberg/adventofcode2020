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
