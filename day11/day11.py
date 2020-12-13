with open("input.txt", "r") as f:
    lines = f.readlines()

seat_status = []
for line in lines:
    seat_status.append(line.rstrip())


def get_adjacent_occupied_count(row, column, seat_status):
    row_range = (max(0, row - 1), row + 2)
    col_range = (max(0, column - 1), column + 2)
    rows = seat_status[row_range[0] : row_range[1]]
    count = 0
    for i in range(len(rows)):
        count += rows[i][col_range[0] : col_range[1]].count("#")
    if seat_status[row][column] == "#":
        count -= 1
    return count


def update_seating(seat_status):
    new_seat_status = seat_status[:]
    for i, row in enumerate(seat_status):
        for j, seat in enumerate(row):
            if not seat == ".":
                count = get_adjacent_occupied_count(i, j, seat_status)
                if seat == "#" and count >= 4:
                    new_seat_status[i] = (
                        new_seat_status[i][:j] + "L" + new_seat_status[i][j + 1 :]
                    )
                elif seat == "L" and count == 0:
                    new_seat_status[i] = (
                        new_seat_status[i][:j] + "#" + new_seat_status[i][j + 1 :]
                    )
    return new_seat_status


new_status = update_seating(seat_status)
iterations = 1
while new_status != seat_status:
    iterations += 1
    seat_status = new_status[:]
    new_status = update_seating(seat_status)


occupied_count = 0
for row in seat_status:
    occupied_count += row.count("#")
print(occupied_count)
