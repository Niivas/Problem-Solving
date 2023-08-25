class Solution:
    def isInterleave(self, s1, s2, s3):
        # Get the lengths of the input strings
        r, c, l = len(s1), len(s2), len(s3)

        # Check if the combined length of s1 and s2 matches s3
        if r + c != l:
            return False

        # Initialize a stack with starting point (0, 0) and a set to keep track of visited indices
        stack, visited = [(0, 0)], {0, 0}

        # Start the depth-first search using the stack
        while stack:
            x, y = stack.pop()  # Pop the current indices from the stack

            # Check if the current indices reach the end of s3
            if x + y == l:
                return True

            # Check if moving right in s1 is valid, and the character matches s3
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                stack.append((x + 1, y))  # Move right in s1
                visited.add((x + 1, y))   # Mark the new indices as visited

            # Check if moving down in s2 is valid, and the character matches s3
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                stack.append((x, y + 1))  # Move down in s2
                visited.add((x, y + 1))   # Mark the new indices as visited

        # If the stack becomes empty and no valid interleaving is found, return False
        return False
