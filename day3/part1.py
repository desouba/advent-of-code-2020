# execute with python ./part1.py

def trees_met(map: list, right: int, down: int):
    trees = 0
    idx_of_column = 0
    idx_of_row = 0
    length_of_row = len(map[0])-1 # so that we do not count the newline character!!!
    while idx_of_row < len(map)-1:
        idx_of_row = idx_of_row + down
        row = map[idx_of_row]
        idx_of_column = idx_of_column + right
        if idx_of_column > length_of_row-1:
            idx_of_column = idx_of_column % length_of_row
        if row[idx_of_column] == '#':
            print("------tree in row", idx_of_row, "column", idx_of_column, ":", row)
            trees = trees + 1
    return trees


if __name__ == '__main__':
    with open("day3.txt") as f:
        map = [str(x) for x in f.readlines()]
        trees_met(map, 3, 1)
