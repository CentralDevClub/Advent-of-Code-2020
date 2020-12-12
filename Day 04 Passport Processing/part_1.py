valid_passport = 0
invalid_passport = 0


def get_key(p_line):
    keys = []
    for i in p_line.split():
        keys.append(i.split(':')[0])
    return keys


def check_validation(keys):
    for_valid = ' '.join(sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']))
    # CID is optional
    if 'cid' in keys:
        keys.remove('cid')

    keys = ' '.join(sorted(keys))
    if for_valid == keys:
        return True
    else:
        return False


with open('passport.txt') as file:
    passport_line = ''
    current_line = True
    while current_line:
        current_line = file.readline()
        if current_line != '\n':
            passport_line += ' ' + current_line[:-1]
        else:
            passport_line = get_key(passport_line)
            if check_validation(passport_line):
                valid_passport += 1
            else:
                invalid_passport += 1
            passport_line = ''
    passport_line = get_key(passport_line)

    if check_validation(passport_line):
        valid_passport += 1
    else:
        invalid_passport += 1
    passport_line = ''

print(f'Valid Passport : {valid_passport}')
print(f'Invalid Passport : {invalid_passport}')
