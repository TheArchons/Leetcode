class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

haystack = input()
needle = input()
print(Solution.strStr(Solution, haystack, needle))