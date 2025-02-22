from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # Hashmap to store the number and its index

        for i, n in enumerate(nums):
            diff = target - n # Calculate the difference between the target and the current number

            if diff in hashMap: # If the difference is in the hashmap, return the index of the difference and the current index
                return [hashMap[diff], i]
            hashMap[n] = i # Add the current number and its index to the hashmap
        return
