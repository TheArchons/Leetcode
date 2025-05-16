class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        newS = ""
        for c in s:
            if c.isalnum():
                newS += c
        
        for i in range(len(newS)//2):
            if newS[i] != newS[len(newS) - i - 1]:
                return False
        
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))