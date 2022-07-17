def numIslands(grid):
    # Treat as a graph. DFS through each node
    # traverse 4 directions (left, right, up, down). Return if out of bounds or water. Add to visited set

    ROWS = len(grid)
    COLS = len(grid[0])
    directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
    count = 0
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or row < 0 or row > ROWS-1 or col < 0 or col > COLS-1: # out of bounds 
            return False
        if grid[row][col] == "W": # Found water
            return False

        visited.add((row, col))
        for dir in directions:
            dfs(row + dir[0], col + dir[1])
        
        return True

    for row in range(ROWS):
        for col in range(COLS):
            if dfs(row, col):
                count += 1
    
    return count



grid1 = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

grid2 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

grid3 = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

print(numIslands(grid2))

assert numIslands(grid1) == 3 
assert numIslands(grid2) == 4
assert numIslands(grid3) == 0
