from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        chars = [(-counter[x], x) for x in counter]

        heapq.heapify(chars)

        reorganized = []
        prev = None
        while len(chars) > 0:
            _, ch = heapq.heappop(chars)

            reorganized.append(ch)
            counter[ch] -= 1

            if prev and counter[prev] > 0:
                heapq.heappush(chars, (-counter[prev], prev))

            prev = ch

        ans = ""
        if counter[prev] == 0:
            ans = "".join(reorganized)
        print(ans)
        return ans