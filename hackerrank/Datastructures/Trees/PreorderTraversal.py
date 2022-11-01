"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    # Write your code here
    visited = set()
    prev = []

    prev.append(-1)  # extra value to traverse to the other side of the parent node
    prev.append(root)
    print(root.info, end=" ")
    curr = root
    while (len(prev) > 0):
        if curr.left is not None and curr.left not in visited:
            curr = curr.left
            print(curr.info, end=" ")
            prev.append(curr)
            visited.add(curr)

        elif curr.right is not None and curr.right not in visited:
            curr = curr.right
            print(curr.info, end=" ")
            prev.append(curr)
            visited.add(curr)

        else:
            curr = prev[-1]
            prev.pop()