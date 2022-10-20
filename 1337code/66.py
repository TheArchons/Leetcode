"""class Solution:
    def roundUp(self, digits, pos):
        if pos < 0:
            digits.insert(0, 1)
            return digits
        else:
            digits[pos] += 1
            if digits[pos] == 10:
                digits[pos] = 0
                return self.roundUp(digits, pos - 1)
            else:
                return digits

    def plusOne(self, digits):
        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1] = 0
            digits = self.roundUp(digits, len(digits) - 2)
        return digits"""

class Solution:
    def plusOne(self, digits):
        #convert digits to int
        num = int(''.join(map(str, digits)))
        num += 1
        #convert num to list of digits
        return [int(x) for x in str(num)]

ins = [int(i) for i in input().strip('[]').split(',')]
print(Solution().plusOne(ins)) 