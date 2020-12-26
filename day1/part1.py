# execute with python ./part1.py

def sum_of_two(numbers: list, sum: int):
    complements = set()  # this is how we initialize a set in python
    for x in numbers:
        complement = sum - x
        if {x}.issubset(complements):
            print('the sum of', str(x), 'and', str(complement), 'is', str(sum))
            return x * complement
        else:
            complements.add(complement)
    return 0  # in case no pair was found which sums to 2020


if __name__ == '__main__':
    with open("day1.txt") as f:
        numbers = [int(x) for x in f.readlines()]
        sum_of_two(numbers, 2020)
