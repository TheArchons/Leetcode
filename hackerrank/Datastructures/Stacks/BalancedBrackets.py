def isBalanced(s):
    # Write your code here
    opens = []
    rev = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for bracket in s:
        if bracket in ['(', '{', '[']:
            opens.append(bracket)
        else:
            if len(opens) == 0:
                return 'NO'
            elif opens.pop() != rev[bracket]:
                return 'NO'
    
    if len(opens) == 0:
        return 'YES'
    else:
        return 'NO'