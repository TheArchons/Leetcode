from collections import deque

class Solution:
    def updateMatrix(self, mat):
        def update(curr, res, row, col):
            if row < 0 or row >= len(res) or col < 0 or col >= len(res[0]) or curr >= res[row][col]:
                return
            
            res[row][col] = curr

            update(curr + 1, res, row - 1, col)
            update(curr + 1, res, row + 1, col)
            update(curr + 1, res, row, col - 1)
            update(curr + 1, res, row, col + 1)

        m = len(mat)
        n = len(mat[0])

        res = []
        q = deque()
        for i in range(m):
            resR = []
            for j in range(n):
                resR.append(10**4 + 1)
                if mat[i][j] == 0:
                    q.append((0, i, j))

            res.append(resR)

        while q:
            curr, row, col = q.popleft()
            if row < 0 or row >= len(res) or col < 0 or col >= len(res[0]) or curr >= res[row][col]:
                continue
            
            res[row][col] = curr
            q.append((curr + 1, row - 1, col))
            q.append((curr + 1, row + 1, col))
            q.append((curr + 1, row, col - 1))
            q.append((curr + 1, row, col + 1))

        return res

sol = Solution()
print(sol.updateMatrix([[1, 1, 0], [1, 0, 0], [1, 1, 1]]))