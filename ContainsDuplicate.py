from typing import List

# (Runtime 15ms) I used the same approach as the TwoSum problem. I created a hash map to store the values of each element in the 'nums' list and used a variable to check if a duplicate number was already stored.
def containsDuplicate(nums: List[int]) -> bool:
        hashMap = {} # Hashmap to store the number and its index

        for i in range(len(nums)):
            duplicate = nums[i] # Get the current number
            if duplicate in hashMap: # If the current number is in the hashmap, return True
                return True
            hashMap[duplicate] = i # Add the current number and its index to the hashmap
        return False

# (Runtime 7ms) I found a better way to solve this problem. Converting the nums list into a set automatically removes duplicates. Then, I simply compare the length of the original nums list with the new set. If the lengths are different, it means there were duplicates, so I return True. Otherwise, I return False.
def containsDuplicateSet(nums: List[int]) -> bool:
        if(len(set(nums)) == len(nums)):
            return False
        return True
