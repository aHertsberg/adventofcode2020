import numpy as np


def parse(seat_str):
    row = seat_str[:7].replace("B", "1").replace("F", "0")
    row = int(row, 2)
    col = seat_str[7:].replace("R", "1").replace("L", "0")
    col = int(col, 2)
    seat_id = row * 8 + col
    return seat_id


with open("input.txt", "r") as f:
    lines = f.readlines()
    seats = []
    for line in lines:
        line = line.rstrip()
        seats.append(parse(line))
    print(max(seats))
    seats = np.array(seats)
    seats.sort()
    dif = np.ediff1d(seats)
    previous_seat = seats[np.where(dif == 2)[0][0]]
    seat_id = previous_seat + 1
    print(seat_id)
