class Solution:
    """
    bfs 
    setup rows, cols variable
    
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [[0,1], [1,0], [0,-1], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        num_islands = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for row_diff, col_diff in moves:
                    new_row, new_col = row + row_diff, col + col_diff
                    if (new_row < 0 or 
                        new_col < 0 or 
                        new_row >= rows or
                        new_col >= cols or
                        grid[new_row][new_col] == "0" or
                        (new_row, new_col) in visited
                    ):
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    num_islands += 1


        return num_islands