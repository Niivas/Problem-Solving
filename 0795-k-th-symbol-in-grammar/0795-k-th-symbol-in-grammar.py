class Solution:
    @staticmethod
    def kthGrammar(n: int, k: int) -> int:
        count = bin(k - 1).count('1')
        return 0 if count % 2 == 0 else 1
