class Solution:
    @staticmethod
    def backspaceCompare(s: str, t: str) -> bool:
        def buildString(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return buildString(s) == buildString(t)
