class Solution:
    @staticmethod
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        # Create a counter of the characters in the ransom note
        r_counter = Counter(ransomNote)

        # Loop through each character in the magazine
        for i in magazine:
            # If the character appears in the ransom note
            if i in r_counter:
                # Decrement the count of the character in the ransom note's counter
                r_counter[i] -= 1
                # If the count of the character reaches zero, remove it from the counter
                if not r_counter[i]:
                    del r_counter[i]

        # If all characters in the ransom note have counts of zero in the counter, return True
        if not len(r_counter):
            return True
        # Otherwise, return False
        return False
