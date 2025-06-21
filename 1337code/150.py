class Solution:
    def evalRPN(self, tokens):
        s = []
        symb = ["+", "-", "*", "/"]

        for tok in tokens:
            if tok in symb:
                second = s.pop()
                first = s.pop()
                if tok == "+":
                    s.append(first + second)
                elif tok == "-":
                    s.append(first - second)
                elif tok == "*":
                    s.append(first * second)
                else:
                    s.append(int(first / second))
            else:
                s.append(int(tok))

        return s.pop()

sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))