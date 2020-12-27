from day3.part1 import trees_met

if __name__ == '__main__':
    with open("day3.txt") as f:
        map = [str(x) for x in f.readlines()]
        product = trees_met(map, 3, 1)*trees_met(map, 1, 1)* trees_met(map, 5, 1)*trees_met(map, 7, 1)*trees_met(map, 1, 2)
        print("product", product)
