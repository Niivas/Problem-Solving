class Solution:
    @staticmethod
    def minFlips(a: int, b: int, c: int) -> int:
        # Calculate the bitwise OR of a and b, then XOR it with c
        # to get the positions where a flip is required.
        flip_positions = (a | b) ^ c

        # Count the number of 1s (flips required) in flip_positions.
        flips_needed = bin(flip_positions).count("1")

        # Calculate the bitwise AND of a and b, then AND it with the
        # bitwise XOR of a, b, and c. This will give the positions where
        # a flip is required due to both a and b having a 1 and c having a 0.
        common_flip_positions = a & b & flip_positions

        # Count the number of additional 1s (flips required) in common_flip_positions.
        common_flips_needed = bin(common_flip_positions).count("1")

        # Add the number of flips required from both cases and return the result.
        return flips_needed + common_flips_needed
