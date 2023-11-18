class Solution:
    @staticmethod
    def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
        # Initialize the search range
        low, high = 1, len(answerKey)

        def is_valid_length(length):
            t_count = 0
            f_count = 0

            # Count occurrences of 'T' and 'F' in the first (length-1) characters
            for i in range(length - 1):
                if answerKey[i] == 'T':
                    t_count += 1
                else:
                    f_count += 1

            left, right = 0, length - 1
            while right < len(answerKey):
                # Update counts for the current window
                if answerKey[right] == 'T':
                    t_count += 1
                else:
                    f_count += 1

                # Check if the current subsequence satisfies the condition
                if min(t_count, f_count) <= k:
                    return True
                else:
                    # Adjust counts and move the window
                    if answerKey[left] == 'T':
                        t_count -= 1
                    else:
                        f_count -= 1
                    left += 1
                    right += 1

            return False

        ans = 1
        while low <= high:
            mid = (low + high) >> 1  # Calculate the middle value

            if is_valid_length(mid):
                ans = mid
                low = mid + 1  # Adjust the low pointer to search for longer subsequences
            else:
                high = mid - 1  # Adjust the high pointer to search for shorter subsequences

        return ans
