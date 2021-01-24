import re


def fields_are_valid(passports: list):
    obligatory_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid_ones = 0
    for x in passports:
        print("!!!!!!")
        fields = re.split('\s+', x)
        passport = {}
        for field in fields:
            (name, value) = re.split(':', field)
            passport[name] = value
        if (obligatory_fields.issubset(passport.keys()) and check_values(passport)):
            valid_ones = valid_ones + 1
    print(valid_ones)


def check_values(passport: dict):
    byr = passport['byr']
    if (re.match(re.compile('\d{4,4}'), byr) is None or int(byr) < 1920 or int(byr)>2002) :
        print("byr", byr)
        return False

    iyr = passport['iyr']
    if (re.match(re.compile('\d{4,4}'), iyr) is None or int(iyr) < 2010 or int(iyr) > 2020):
        print("iyr", iyr)
        return False

    eyr = passport['eyr']
    if (re.match(re.compile('\d{4,4}'), eyr) is None or int(eyr) < 2020 or int(eyr) > 2030):
        print("eyr", eyr)
        return False

    hgt = passport['hgt'] ####SOS
    value_cm = re.search(('(\d+)[cm]'), hgt)
    value_in = re.search(('(\d+)[in]'), hgt)
    if not value_cm and not value_in:
        print("hgt", hgt)
        return False
    if value_in:
        if 59 > int(value_in.group(1)) > 76:
            print("hgt", hgt)
            return False
    if value_cm:
        if 150 > int(value_cm.group(1)) > 193:
            print("hgt", hgt)
            return False

    hcl = passport['hcl']
    if (re.match(re.compile('(#){1}[0-9|a-f]{6}'), hcl) is None ):
        print("hcl:",hcl)
        return False

    ecl = passport['ecl']
    if (re.match(re.compile('amb|blu|brn|gry|grn|hzl|oth'), ecl) is None):
        print("ecl:",ecl)
        return False

    pid = passport['pid']
    if (re.match(re.compile('[0-9]{9}'), pid) is None):
        print("pid:",pid)
        return False

    return True


if __name__ == '__main__':
    with open("day4.txt") as f:
        contents = f.read()
        passports = re.split('\n\s*\n', contents)
        fields_are_valid(passports)
