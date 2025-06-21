class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        def dfs(curr, node, visited):
            if curr.val in visited:
                return
            
            visited[curr.val] = curr
            
            for neighbor in node.neighbors:
                if neighbor.val in visited:
                    curr.neighbors.append(visited[neighbor.val])
                else:
                    n = Node(neighbor.val, [])
                    curr.neighbors.append(n)
                    dfs(n, neighbor, visited)
        
        if node is None:
            return None
        visited = {}
        res = Node(node.val, [])
        dfs(res, node, visited)
        return res

sol = Solution()

# test
# adjList = [[2,4],[1,3],[2,4],[1,3]]
# make based on this

# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

# Connect neighbors according to adjList = [[2,4],[1,3],[2,4],[1,3]]
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

n = n1

res = sol.cloneGraph(n)
print(res.val)