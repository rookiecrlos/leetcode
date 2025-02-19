from typing import List

# (Runtime 9ms) I realized I didn't need to create a new variable. The same iteration can be stored in the hash map to compare the current value with the previously stored ones.
def containsDuplicate(nums: List[int]) -> bool:
        hashMap = {} # Hashmap to store the number and its index

        for i in range(len(nums)):
            if nums[i] in hashMap: # If the current number is in the hashmap, return True
                return True
            hashMap[nums[i]] = i # Add the current number and its index to the hashmap
        return False

# (Runtime 7ms) I found a better way to solve this problem. Converting the nums list into a set automatically removes duplicates. Then, I simply compare the length of the original nums list with the new set. If the lengths are different, it means there were duplicates, so I return True. Otherwise, I return False.
def containsDuplicateSet(nums: List[int]) -> bool:
        if(len(set(nums)) == len(nums)):
            return False
        return True
