class Solution:
    @staticmethod
    def removeDuplicateLetters(s: str) -> str:   
        last_occ = {}
        stack = []
        visited = set()

        for i, item in enumerate(s):
            last_occ[item] = i

        for i, item in enumerate(s):
            if item not in visited:
                while (stack and stack[-1] > item and last_occ[stack[-1]] > i):
                    visited.remove(stack.pop())
                stack.append(item)
                visited.add(item)

        return ''.join(stack)
