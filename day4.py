import re

def byr(data):
    try:
        i = int(data)
        return i >= 1920 and i <= 2002
    except ValueError:
        return False

def iyr(data):
    try:
        i = int(data)
        return i >= 2010 and i <= 2020
    except ValueError:
        return False

def eyr(data):
    try:
        i = int(data)
        return i >= 2020 and i <= 2030
    except ValueError:
        return False

def hgt(data):
    if re.match('^[\d]+cm$', data):
        i = int(data[:-2])
        return i >= 150 and i <= 193
    elif re.match('^[\d]+in$', data):
        i = int(data[:-2])
        return i >= 59 and i <= 76
    return False

def hcl(data):
    return re.match('^#[a-f\d]{6}$', data)

ecl_set = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
}

def ecl(data):
    return data in ecl_set

def pid(data):
    return re.match('^[\d]{9}$', data)


field_to_func = {
    'byr':byr,
    'iyr':iyr,
    'eyr':eyr,
    'hgt':hgt,
    'hcl':hcl,
    'ecl':ecl,
    'pid':pid,
}

required_fields = {s for s in field_to_func.keys()}


with open('inputs/day4.txt', 'r') as file:
    passports = file.read().split('\n\n')
    num_present = 0
    num_valid = 0
    for passport in passports:
        fields = passport.split()
        S = set()
        is_valid = True
        for k, v in [field.split(':') for field in fields]:
            if k in field_to_func:
                S.add(k)
                if not field_to_func[k](v):
                    is_valid = False
        if required_fields.issubset(S):
            num_present += 1
            if is_valid:
                num_valid += 1
    print(f"There are {num_present} passports with valid fields, of which {num_valid} have valid data.")
    