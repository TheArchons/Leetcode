from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        def isValid(row, col):
            return row < len(grid) and row >= 0 and col < len(grid[0]) and col >= 0 and grid[row][col] == 1
        
        initRots = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    initRots.append((row, col))
        
        q = deque([initRots])
        
        dayCount = 0

        while (True):
            todayRotten = q.popleft()
            tmrwRotten = []
            for rot in todayRotten:
                dirs = [
                    (rot[0] - 1, rot[1]),
                    (rot[0] + 1, rot[1]),
                    (rot[0], rot[1] - 1),
                    (rot[0], rot[1] + 1)
                ]

                for nextR, nextC in dirs:
                    if isValid(nextR, nextC):
                        grid[nextR][nextC] = 2
                        tmrwRotten.append((nextR, nextC))
            
            if tmrwRotten:
                q.append(tmrwRotten)
                dayCount += 1
            else:
                break
        
        return dayCount

sol = Solution()
# [[2,1,1],[1,1,0],[0,1,1]]

grid = [[2,1,1],[1,1,0],[0,1,1]]

print(sol.orangesRotting(grid))