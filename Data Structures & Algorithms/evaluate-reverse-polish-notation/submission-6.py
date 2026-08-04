from operator import add, sub, mul, truediv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        l1 = ["+","-","*","/"]
        for i in range(len(tokens)):
            s = ""
            if tokens[i] in l1:
                y = int(stack.pop())
                x = int(stack.pop())

                if tokens[i] == "+":
                    stack.append(x+y)
                elif tokens[i] == "-":
                    stack.append(x-y)
                elif tokens[i] == "*":
                    stack.append(x*y)
                elif tokens[i] == "/":
                    stack.append(x/y)

            else:
                stack.append(tokens[i])

            
        return int(stack[0])



        