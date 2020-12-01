import numpy as np
from datetime import datetime


def calculate(numbers):
    i = 0
    j = len(numbers) - 1

    while i < j:
        num_sum = numbers[i] + numbers[j]
        if num_sum == 2020:
            return numbers[i] * numbers[j]
        elif num_sum < 2020:
            i += 1
        else:
            j -= 1
    return False


def calculate_3(numbers):
    for k in numbers:
        i = 0
        j = len(numbers) - 1

        while i < j:
            num_sum = numbers[i] + numbers[j] + k
            if num_sum == 2020:
                return numbers[i] * numbers[j] * k
            elif num_sum < 2020:
                i += 1
            else:
                j -= 1
    return False


start=datetime.now()


with open('input.txt', 'r') as content:
    numbers = content.readlines()
    numbers = [x[:-1] for x in numbers]
    numbers = map(int, numbers)
    numbers = np.array(list(numbers))
    numbers.sort()
    print(calculate_3(numbers))


print(datetime.now()-start)
