
import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_between(x, begin, end):
    return begin <= int(x) <= end

def valid_birth_year(byr):
    return is_between(byr, 1920, 2002)

def valid_issue_year(iyr):
    return is_between(iyr, 2010, 2020)

def valid_exp_year(eyr):
    return is_between(eyr, 2020, 2030)

def valid_height(hgt):
    unit = hgt[-2:]
    numeric = hgt[:-2]
    if unit == 'in':
        return is_between(numeric, 59, 76)
    elif unit == 'cm':
        return is_between(numeric, 150, 193)
    return False

def valid_hair_color(hcl):
    regex = re.compile(r'#[0-9a-f]{6}$')
    return True if regex.search(hcl) else False

def valid_eye_color(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_passport_id(pid):
    regex = re.compile(r'^[0-9]{9}$')
    return True if regex.search(pid) else False

field_validator_map = {
    'byr': valid_birth_year, 
    'iyr': valid_issue_year, 
    'eyr': valid_exp_year, 
    'hgt': valid_height, 
    'hcl': valid_hair_color, 
    'ecl': valid_eye_color, 
    'pid': valid_passport_id}

def is_valid_field_value(field, value):
    return field_validator_map[field](value)

def solve():
    passport = {}
    invalid_count = 0
    valid_count = 0

    with open('data/day_4_input.txt', 'r') as f:
        for line in f:
            if (line == '\n'):
                if is_valid_passport(passport):
                    valid_count += 1
                else:
                    invalid_count += 1 
                passport = {}
            else:
                data = line[:-1].split(' ')
                for d in data:
                    k, v = d.split(':')
                    passport[k] = v 

    return f"{invalid_count} invalid passports found, {valid_count} valid passports found"
                

def is_valid_passport(p):
    for field in required_fields:
        val = p.get(field)
        if not val or not is_valid_field_value(field, val):
            return False
        
    return True


print(solve())


### Part I 
# 264 is too high
# 64 is not right

### Part II
# 117 is too high