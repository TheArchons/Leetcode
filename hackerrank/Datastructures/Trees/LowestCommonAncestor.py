def findPath(root, v):
    path = []
    while root.info != v:
        path.append(root)
        if v < root.info:
            root = root.left
        else:
            root = root.right
    
    path.append(root)
    return path

def lca(root, v1, v2):
    path1 = findPath(root, v1)
    path2 = findPath(root, v2)

    if len(path1) < len(path2):
        temp = path1
        path1 = path2
        path2 = temp

    path2Set = set(path2)

    for node in reversed(path1):
        if node in path2Set:
            return node
