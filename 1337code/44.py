class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        
        breakOut = False
        while len(s) > 0:
            if len(p) == 0:
                return False
            elif p[0] == s[0] or p[0] == '?':
                s = s[1:]
                p = p[1:]
            elif p[0] == '*':
                if len(p) == 1:
                    return True
                else:
                    for pos, c in enumerate(s):
                        if c == p[1]:
                            breakOut = True
                            s = s[pos+1:]
                            p = p[2:]
                            break
                    if breakOut:
                        breakOut = False
                        continue
            else:
                return False
        if len(p.replace("*", '')) == 0 and len(s) == 0:
            return True
        return False


print(Solution().isMatch(input().strip('"'), input().strip('"')))