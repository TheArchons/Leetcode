def decodeHuff(root, s):
    curr = root
    for i in s:
        if i == '0':
            if curr.left.data == '\0':
                curr = curr.left
            else:
                print(curr.left.data, end='')
                curr = root
        else:
            if curr.right.data == '\0':
                curr = curr.right
            else:
                print(curr.right.data, end='')
                curr = root