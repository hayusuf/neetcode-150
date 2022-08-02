"""
Two Sum
- solved using hashmap
- iterated through elements and
  checked if complememnt was added
  to hashmap, if not then add current
  element to hashmap until both elements
  are iterated to.

time complexity:    O(N)
space complexity:   O(N)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap= {}
        for i,n in enumerate(nums):
            complement = target-n
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[n]=i
