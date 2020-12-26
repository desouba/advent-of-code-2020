# execute with python ./part1.py

def valid_password(passwords: list):
    valid = 0
    for x in passwords:
        split = x.split()
        minmax = split[0].split("-")
        min = int(minmax[0])
        max = int(minmax[1])
        letter = split[1][:-1]
        password = split[2]
        print(min, max, letter, split[2])
        if ((password[min-1] == letter) and (password[max-1] != letter)) or ((password[min-1] != letter) and (password[max-1] == letter)):
            valid = valid + 1
    print(valid)


if __name__ == '__main__':
    with open("day2.txt") as f:
        numbers = [str(x) for x in f.readlines()]
        valid_password(numbers)
