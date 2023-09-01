from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a list to store the count of set bits for each number from 0 to n.
        result = [0]*(n+1)

        # Iterate through each number from 0 to n.
        for i in range(n+1):
            # Call the countSetBits method to count the set bits in the current number i.
            result[i] = self.countSetBits(i)

        # Return the list containing the count of set bits for each number.
        return result

    def isSetBit(self, n: int, k: int) -> bool:
        # Check if the k-th bit of the number n is set (1).
        return (n >> k & 1) == 1

    def countSetBits(self, n: int):
        count = 0
        # Iterate through each bit position (from 0 to 30) in the number.
        for i in range(31):
            # If the current bit is set, increment the count.
            if self.isSetBit(n, i):
                count += 1
        # Return the total count of set bits in the number.
        return count