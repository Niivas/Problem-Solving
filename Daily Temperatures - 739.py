from typing import List
class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [(temperatures[-1], n-1)]  # Initialize stack with last temperature and its index
        ans = [0] * n  # Initialize answer array with zeros
        ans[-1] = 0  # No warmer days for the last day

        # Loop through the temperatures in reverse order
        for i in range(n-2, -1, -1):
            # Check if the current day's temperature is lower than the next day's temperature
            if temperatures[i] < temperatures[i+1]:
                stack.append((temperatures[i], i))
                ans[i] = 1
            else:
                # Remove temperatures from stack that are not warmer than current day's temperature
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()

                # If no warmer day is found in the remaining days, mark ans[i] as 0
                if len(stack) == 0:
                    ans[i] = 0
                else:
                    # Calculate the number of days until a warmer day
                    ans[i] = stack[-1][1] - i

                stack.append((temperatures[i], i))  # Add current day's temperature to the stack

        return ans
