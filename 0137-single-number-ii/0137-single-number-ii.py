class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the variable to hold the single number
        single_number = 0

        # Iterate over each bit position (0 to 31)
        for bit_position in range(32):
            # Count the number of occurrences of the current bit position in the array
            count = 0
            for num in nums:
                
                count += (num >> bit_position) & 1

            # If the count modulo 3 is 1, it means the single number has a set bit at this position
            if count % 3 == 1:
                # Set the bit in the single_number variable
                single_number = single_number | (1 << bit_position)
            
        if single_number >= 2**31:
            single_number -= 2**32

        # Return the single number
        return single_number
