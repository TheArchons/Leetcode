class Solution: #this one was just annoying
    def myAtoi(self, s: str) -> int:
        #remove all the spaces
        isNegative = False
        s = s.strip()
        integer = ""
        for pos, i in enumerate(s):
            try:
                int(i)
                integer += i
            except:
                if (i == "-") and pos == 0:
                    isNegative = True
                    continue
                elif (i == "+") and pos == 0:
                    continue
                break
        integer = int(integer) if integer != "" else 0
        if isNegative:
            integer = -integer
        if integer > 2**31 - 1:
            return 2**31 - 1
        elif integer < -2**31:
            return -2**31
        else:
            return integer

inStr = input()
print(Solution().myAtoi(inStr))