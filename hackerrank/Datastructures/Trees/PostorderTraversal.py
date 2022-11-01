def postOrder(root):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack[-1]
        if node.left is not None:
            stack.append(node.left)
            node.left = None
        elif node.right is not None:
            stack.append(node.right)
            node.right = None
        else:
            print(node.info, end=" ")
            stack.pop()
