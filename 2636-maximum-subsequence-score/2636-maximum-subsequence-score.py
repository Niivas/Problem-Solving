import heapq
class Solution:
    def maxScore(self, A, B, k):
        total_score = 0  # Total score of selected elements
        max_score = 0  # Maximum score

        heap = []  # Heap to store elements

        # Create a list of tuples by zipping arrays A and B, and sort it based on B values in descending order
        sorted_elements = sorted(zip(A, B), key=lambda ab: -ab[1])

        # Iterate over the sorted list of tuples
        for a, b in sorted_elements:
            heapq.heappush(heap, a)  # Push the current element into the heap
            total_score += a  # Add the current element to the total score

            if len(heap) > k:
                smallest = heapq.heappop(heap)  # Remove the smallest element from the heap
                total_score -= smallest  # Subtract the popped value from the total score

            if len(heap) == k:
                score = total_score * b  # Calculate the score by multiplying total score with current B value
                max_score = max(max_score, score)  # Update the maximum score if the calculated score is greater

        return max_score  # Return the maximum score