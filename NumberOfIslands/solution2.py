from asset.meta_grid import grid1

'''
Solution2 is an improvement from Solution 1.
It will not change the original grid input but use a set to maintain the visited land cells.
'''


def NumberOfIslands(input_grid):
    count = 0
    visited = set()  # store the visited land cells
    # print(len(visited))
    if len(input_grid) == 0:
        return count
    else:
        for m in range(len(input_grid)):
            for n in range(len(input_grid[0])):
                if input_grid[m][n] == 1 and (
                        m, n) not in visited:  # only check land cells that is not in the visited set
                    dfs(input_grid, m, n, visited)
                    count += 1
    return count


def dfs(gird, m, n, visited):
    if m < 0 or n < 0 or m >= len(gird) or n >= len(gird[0]) or gird[m][n] != 1 or (m, n) in visited:
        return
    else:
        visited.add((m, n))

        '''check four neighbors'''
        dfs(gird, m + 1, n, visited)
        dfs(gird, m - 1, n, visited)
        dfs(gird, m, n + 1, visited)
        dfs(gird, m, n - 1, visited)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(NumberOfIslands(input_grid=grid1()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
