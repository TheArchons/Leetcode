def isValid(s):
    stack = []
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False
print(isValid(input()))