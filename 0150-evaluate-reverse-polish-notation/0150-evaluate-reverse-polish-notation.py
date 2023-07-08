class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack and a variable to keep track of the current index
        stack = []
        cur = 0

        # Evaluate the RPN expression
        while len(stack) > 1 or cur < len(tokens):
            # Check the current token
            if tokens[cur] == "+":
                # Addition operation
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif tokens[cur] == "-":
                # Subtraction operation
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tokens[cur] == "*":
                # Multiplication operation
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif tokens[cur] == "/":
                # Division operation
                a = stack.pop()
                b = stack.pop()
                if b / a < 0:
                    stack.append(math.ceil(b / a))
                else:
                    stack.append(math.floor(b / a))
            else:
                # Token is a number, convert it to an integer and push to the stack
                stack.append(int(tokens[cur]))
            cur += 1

        # Return the result
        return stack[0]
