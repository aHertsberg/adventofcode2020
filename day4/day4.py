# Oh my goodness this is ugly. Separate functions for each key?
def validate(key, value):
    if key == "byr":
        value = int(value)
        if value >= 1920 and value <= 2002:
            return True
    if key == "iyr":
        value = int(value)
        if value >= 2010 and value <= 2020:
            return True
    if key == "eyr":
        value = int(value)
        if value >= 2020 and value <= 2030:
            return True
    if key == "hgt":
        unit = value[-2:]
        try:
            value = int(value[:-2])
        except ValueError:
            return False
        if unit == "cm" and value >= 150 and value <= 193:
            return True
        elif unit == "in" and value >= 59 and value <= 76:
            return True
    if key == "hcl":
        if value[0] == "#" and len(value) == 7:
            try:
                int(value[1:], 16)
                return True
            except ValueError:
                return False
    if key == "ecl":
        permitted_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value in permitted_colors:
            return True
    if key == "pid":
        if len(value) == 9:
            try:
                int(value)
                return True
            except ValueError:
                return False
    if key == "cid":
        return True
    return False


with open("input.txt", "r") as f:
    lines = f.readlines()
    passports = []
    entry = {}
    for line in lines:
        if len(line) <= 1 and len(entry) > 0:
            passports.append(entry)
            entry = {}
        elif len(line) > 1:
            fields = line.rstrip().split(" ")
            for field in fields:
                key, value = field.split(":")
                entry[key] = value

    sufficient_count = 0
    valid_count = 0
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for entry in passports:
        is_sufficient_entry = True
        keys = list(entry)
        for key in required_keys:
            if not key in keys:
                is_sufficient_entry = False
        if is_sufficient_entry:
            sufficient_count += 1
            has_valid_fields = True
            for key in keys:
                if not validate(key, entry[key]):
                    has_valid_fields = False
            if has_valid_fields:
                valid_count += 1
    print(sufficient_count)
    print(valid_count)
