def check_binary_search_tree_(root):
    # dfs
    curr = root
    prev = [curr]
    visited = set()

    while (prev):
        if (curr.left is not None and curr.left.data > curr.data) and (curr.right is not None and curr.right.data < curr.data):
            return False
        if curr.left is not None and curr.left not in visited:
            prev.append(curr)
            curr = curr.left
        elif curr.right is not None and curr.right not in visited:
            prev.append(curr)
            curr = curr.right
        else:
            visited.add(curr)
            curr = prev.pop()
    
    return True
