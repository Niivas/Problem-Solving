import math
class Solution:
    @staticmethod
    def isPowerOfFour(num: int) -> bool:
        return (num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0)