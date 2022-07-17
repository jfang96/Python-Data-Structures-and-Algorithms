def smallestIsland(grid):
    # Treat as a graph. DFS through each node
    # traverse 4 directions (left, right, up, down). Return if out of bounds or water. Add to visited set

    ROWS = len(grid)
    COLS = len(grid[0])
    directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
    minIsland = float('inf')
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or row < 0 or row > ROWS-1 or col < 0 or col > COLS-1: # out of bounds 
            return 0
        if grid[row][col] == "W": # Found water
            return 0

        size = 1
        visited.add((row, col))
        for dir in directions:
            size += dfs(row + dir[0], col + dir[1])
        
        return size

    for row in range(ROWS):
        for col in range(COLS):
            size = dfs(row, col)
            if size > 0: 
                minIsland = min(minIsland, size)

    return minIsland



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
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

grid4 = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

assert smallestIsland(grid1) == 2 
assert smallestIsland(grid2) == 1
assert smallestIsland(grid3) == 9
assert smallestIsland(grid4) == 1
