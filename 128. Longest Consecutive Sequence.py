from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a new sequence
            current_streak = 1

            while num + 1 in num_set:  # Count consecutive numbers
                num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest
