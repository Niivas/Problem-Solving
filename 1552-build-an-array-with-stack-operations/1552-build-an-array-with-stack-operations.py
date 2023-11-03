class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 1
        for num in target:
            while i < num:
                res.append("Push")
                res.append("Pop")
                i += 1
            res.append("Push")
            i += 1
        return res