with open("input.txt", "r") as f:
    lines = f.readlines()

program_sequence = []
for line in lines:
    line = line.rstrip()
    operand, value = line.split(" ")
    value = int(value)
    program_sequence.append((operand, value))

i = 0
running_sequence = []
acc = 0
while not i in running_sequence:
    running_sequence.append(i)
    operand, value = program_sequence[i]
    if operand == "acc":
        acc += value
        i += 1
    elif operand == "nop":
        i += 1
    else:  # jump
        i += value

print(acc)
