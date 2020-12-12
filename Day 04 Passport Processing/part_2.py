class Passport:
    def __init__(self, path):
        self.valid_passport = 0
        self.invalid_passport = 0
        self.passports = []
        self.raw_passports = []
        with open(path) as file:
            self.lines = file.readlines()

    def show(self):
        if len(self.passports) > 0:
            for i in self.passports:
                print([i])
        elif len(self.raw_passports) > 0:
            for i in self.raw_passports:
                print([i])
        else:
            for i in self.lines:
                print([i])

    def process(self):
        # Step 1: Extract to string
        one_passport = ''
        for line in self.lines:
            if line == '\n':
                self.raw_passports.append(one_passport)
                one_passport = ''
            else:
                one_passport += line[:-1] + ' '
        self.raw_passports.append(one_passport)

        # Step 2: From string to dictionary
        for line in self.raw_passports:
            temp_passport = {}
            for data in line.split():
                key_value = data.split(':')
                temp_passport[key_value[0]] = key_value[1]
            self.passports.append(temp_passport)
        return self

    @staticmethod
    def valid_int(value_str, bottom, top):
        value = int(value_str)
        if value < bottom or value > top:
            return False
        else:
            return True

    def validate(self):

        """
        - byr (Birth Year) - four digits; at least 1920 and at most 2002.\n
        - iyr (Issue Year) - four digits; at least 2010 and at most 2020.\n
        - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.\n
        - hgt (Height) - a number followed by either cm or in:\n
        - If cm, the number must be at least 150 and at most 193.\n
        - If in, the number must be at least 59 and at most 76.\n
        - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.\n
        - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.\n
        - pid (Passport ID) - a nine-digit number, including leading zeroes.\n
        - cid (Country ID) - ignored, missing or not.
        """

        for clean_passport in self.passports:
            valid_requirement = 0
            for key, value in clean_passport.items():
                if key == 'byr':
                    if self.valid_int(value, 1920, 2002):
                        valid_requirement += 1
                elif key == 'iyr':
                    if self.valid_int(value, 2010, 2020):
                        valid_requirement += 1
                elif key == 'eyr':
                    if self.valid_int(value, 2020, 2030):
                        valid_requirement += 1
                elif key == 'hgt':
                    if value[-2:] == 'cm':
                        if self.valid_int(value[:-2], 150, 193):
                            valid_requirement += 1
                    elif value[-2:] == 'in':
                        if self.valid_int(value[:-2], 59, 76):
                            valid_requirement += 1
                elif key == 'hcl':
                    if value[0] == '#':
                        if len(value) == 7:
                            valid_requirement += 1
                elif key == 'ecl':
                    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        valid_requirement += 1
                elif key == 'pid':
                    if len(value) == 9:
                        valid_requirement += 1

            if valid_requirement == 7:
                self.valid_passport += 1
            else:
                self.invalid_passport += 1
        return self

    def see_validation(self):
        print(f'Valid Passport : {self.valid_passport}')
        print(f'Invalid Passport : {self.invalid_passport}')


passport = Passport('passport.txt')
passport.process().validate().see_validation()
