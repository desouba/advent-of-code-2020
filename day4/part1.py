import re


def obligatory_fields_exist(passports:list):
    obligatory_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_ones = 0
    for x in passports:
        fields = re.split('\s+', x)
        passport = {}
        for field in fields:
            (name, value) = re.split(':', field)
            passport[name] = value
        if obligatory_fields.issubset(passport.keys()):
            valid_ones = valid_ones+1
    print(valid_ones) # 202

if __name__ == '__main__':
    with open("day4.txt") as f:
        contents = f.read()
        passports = re.split('\n\s*\n', contents)
        for x in passports:
            print('-----')
            print(x)
        obligatory_fields_exist(passports)
