class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_of_islands = 0
        visited = set() # store grid position (i,j)

        def bfs(row, col):
            moves = [[1,0], [-1,0], [0,1], [0,-1]]
            q = collections.deque() # [ (0,4) ]
            q.append((row,col))
            visited.add((row,col))  # { (0,0), (1,0), (0,1), (1,1), (0,4) }

            while q:
                curr_row, curr_col = q.popleft()    # 0, 4
                for row_diff, col_diff in moves:    # 1, 0
                    new_row = curr_row + row_diff   
                    new_col = curr_col + col_diff   # 1, 0

                    if (0 <= new_row < rows and
                        0 <= new_col < cols and 
                        (new_row,new_col) not in visited and
                        grid[new_row][new_col] == "1"
                    ):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                    


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    num_of_islands += 1
                    bfs(i, j)

        return num_of_islands