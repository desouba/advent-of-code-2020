# execute with python ./part1.py

def valid_password(passwords: list):
    valid = 0
    for x in passwords:
        split = x.split()
        minmax = split[0].split("-")
        min = minmax[0]
        max = minmax[1]
        letter = split[1][:-1]
        password = split[2]
        # print(min, max, split[1][:-1], split[2])
        freq = 0
        for p in password:
            if p == letter:
                freq = freq + 1
        if (freq >= int(min)) and (freq <= int(max)):
            valid = valid + 1
    print(valid)


if __name__ == '__main__':
    with open("day2.txt") as f:
        numbers = [str(x) for x in f.readlines()]
        valid_password(numbers)
