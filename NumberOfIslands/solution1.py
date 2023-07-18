from asset.meta_grid import grid1

'''
Solution1 use the dfs to explore the cell of lands.
The initial input will be changed after running the script
'''


def NumberOfIslands(input_grid):
    count = 0
    if len(input_grid) == 0:
        return count
    else:
        for m in range(len(input_grid)):
            for n in range(len(input_grid[0])):
                if input_grid[m][n] == 1:  # only check cell of lands
                    dfs(input_grid, m, n)
                    count += 1
    return count


def dfs(new_grid, m, n):
    if m < 0 or n < 0 or m >= len(new_grid) or n >= len(new_grid[0]) or new_grid[m][n] != 1:
        return
    else:
        new_grid[m][n] = "#"

        '''check four neighbors'''
        dfs(new_grid, m + 1, n)
        dfs(new_grid, m - 1, n)
        dfs(new_grid, m, n + 1)
        dfs(new_grid, m, n - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(NumberOfIslands(input_grid=grid1()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
