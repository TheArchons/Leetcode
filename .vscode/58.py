"""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        return len(s[-1]) if s else 0"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #go through all whitespace
        pos = len(s)-1
        while pos >= 0 and s[pos] == ' ':
            pos -= 1
        if pos < 0:
            return 0
        
        start = pos
        #find the next space
        while pos >= 0 and s[pos] != ' ':
            pos -= 1
        return start - pos

print(Solution.lengthOfLastWord(Solution, input()))