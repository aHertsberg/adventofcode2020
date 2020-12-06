with open("input.txt", "r") as f:
    lines = f.readlines()
or_answers = []  # logical or, every unique character counts
and_answers = []  # logical and, every character that is present in all lines count
or_string = ""
first_entry = True

for line in lines:
    line = line.rstrip()
    if len(line) > 0:
        if first_entry:
            and_string = line
            first_entry = False
        else:
            for char in and_string:
                if not char in line:
                    and_string = and_string.replace(char, "")

        for char in line:
            if not char in or_string:
                or_string += char

    else:
        or_answers.append(or_string)
        and_answers.append(and_string)
        or_string = ""
        first_entry = True
or_answers.append(or_string)
and_answers.append(and_string)

or_sum = 0
for ans in or_answers:
    or_sum += len(ans)
print(or_sum)

and_sum = 0
for ans in and_answers:
    and_sum += len(ans)
print(and_sum)
