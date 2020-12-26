# execute with python ./part1.py
import part1


def sum_of_three(numbers: list):
    for current in range(len(numbers)):
        product = part1.sum_of_two(numbers[current + 1:len(numbers)], 2020 - numbers[current])
        if product > 0:  # pair found
            print("third number: " + str(numbers[current]))
            print (product*numbers[current])


if __name__ == '__main__':
    with open("day1.txt") as f:
        numbers = [int(x) for x in f.readlines()]
        sum_of_three(numbers)
