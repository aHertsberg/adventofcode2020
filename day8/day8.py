with open("input.txt", "r") as f:
    lines = f.readlines()

program_sequence = []
for line in lines:
    line = line.rstrip()
    operand, value = line.split(" ")
    value = int(value)
    program_sequence.append([operand, value])


def run_program(program_sequence, modified_program=False):
    i = 0
    running_sequence = []
    acc = 0
    state = False
    program_length = len(program_sequence)
    while not i in running_sequence and i < program_length:
        running_sequence.append(i)
        operand, value = program_sequence[i]
        if operand == "acc":
            acc += value
            i += 1
        elif operand == "nop":
            i += 1
        else:  # jump
            i += value

        if i == len(program_sequence):
            state = True
    if not state:
        if modified_program:
            acc = False
        else:
            print("Program entered loop with accumulator value {}".format(acc))
    return acc


run_program(program_sequence)

for i in range(len(program_sequence)):
    operand = program_sequence[i][0]
    if operand == "nop":
        program_sequence[i][0] = "jmp"
    else:
        program_sequence[i][0] = "nop"
    exit_status = run_program(program_sequence, modified_program=True)
    if type(exit_status) == int:
        print("Accumulator value at end of program after fix: {}".format(exit_status))
    program_sequence[i][0] = operand  # undo changed line
