class Solution:
    """
    Input: grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    setup counter
    setup visited set
    loop i in range of rows
    loop j in range of cols
    check if element is 0 or visited
        if yes, continue
        if no, we found land
            increment counter
            bfs to mark connected land as visited
    return counter
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        counter = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while q:
                row, col = q.popleft()
                for row_diff, col_diff in directions:
                    new_row, new_col = row + row_diff, col + col_diff
                    
                    if not (0 <= new_row < rows and 
                        0 <= new_col < cols and
                        grid[new_row][new_col] == "1" and
                        (new_row,new_col) not in visited):
                        continue
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
                        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    counter += 1
                    bfs(i, j)

        return counter
