def count():
    matches = 0

    for row in open('input.txt', 'r'):
        row = row.rstrip()
        parts = row.split(' ')

        numbers = parts[0].split('-')
        minimum = int(numbers[0])
        maximum = int(numbers[1])

        character = parts[1][0]

        pw = parts[2]

        count = 0
        for x in pw:
            if x == character:
                count += 1

        if count >= minimum and count <= maximum:
            matches += 1

    return(matches)


def unique_position():
    matches = 0

 
    for row in open('input.txt', 'r'):
        row = row.rstrip()
        parts = row.split(' ')

        numbers = parts[0].split('-')
        first = int(numbers[0])
        second = int(numbers[1])

        character = parts[1][0]
        pw = parts[2]

        legit = False

        if pw[first - 1] == character:
            legit = not legit
        if pw[second - 1] == character:
            legit = not legit
        
        if legit:
            matches += 1

    return matches 



print(unique_position())
