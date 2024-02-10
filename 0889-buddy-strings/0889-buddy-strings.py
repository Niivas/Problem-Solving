from collections import Counter

class Solution:
    @staticmethod
    def buddyStrings(s: str, goal: str) -> bool:
        # Check if s is equal to goal and if all characters in s are unique
        if s == goal and len(set(s)) == len(s):
            return False

        # Check if character counts of s and goal are different
        if Counter(s) != Counter(goal):
            return False

        count = 0
        i = 0
        j = 0

        # Iterate over s and goal
        while i < len(s) and j < len(goal):
            if s[i] == goal[j]:
                # Characters at current positions are equal, increment both pointers
                i += 1
                j += 1
            else:
                # Characters at current positions are different, increment count and both pointers
                count += 1
                i += 1
                j += 1

            # Check if count exceeds 2, return False
            if count > 2:
                return False

        # Check if both pointers have reached the end of their respective strings
        if i != len(s) or j != len(goal):
            return False

        # Return True if all conditions are passed
        return True
