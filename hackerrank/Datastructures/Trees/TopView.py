class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    prev = [[root, False]]
    visited = set()
    curr = root
    vertical = horizontal = 0
    heights = {}
    while (len(prev) != 0):
        if (horizontal not in heights or heights[horizontal][1] < vertical):
            heights[horizontal] = (curr.info, vertical)
        if (curr.left is not None and curr.left not in visited):
            curr = curr.left
            prev.append([curr, True])
            visited.add(curr)
            horizontal -= 1
            vertical -= 1
        elif (curr.right is not None and curr.right not in visited):
            curr = curr.right
            prev.append([curr, False])
            visited.add(curr)
            horizontal += 1
            vertical -= 1
        else:
            if (prev[-1][1]):
                horizontal += 1
            else:
                horizontal -= 1
            prev.pop()
            if (len(prev) != 0):
                curr = prev[-1][0]
                vertical += 1
        
    for i in sorted(heights):
        print(heights[i][0], end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)

"""
6
1 2 5 3 6 4
"""