def ride_toboggan(rows, step_right, step_down):
    count = 0
    pos_x = 0
    pos_y = 0
    for row in rows:
        row = row.rstrip()
        if (pos_y % step_down) == 0:
            index = pos_x % len(row)
            if row[index] == "#":
                count += 1
            pos_x += step_right
        pos_y += 1
    return count


with open("input.txt", "r") as f:
    lines = f.readlines()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (7, 2)]
    result = 1
    for slope in slopes:
        result *= ride_toboggan(lines, slope[0], slope[1])
    print(result)
