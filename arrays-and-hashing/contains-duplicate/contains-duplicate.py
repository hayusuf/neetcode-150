"""
Contains Duplicate

- solved using hashset
- iterated through elements and
  checked if item already exists in hashset,
  if so return true, if not add element to 
  hashset.

Best solution:
time complexity:    O(N)
space complexity:   O(N)
"""

class Solution(object):
    def containsDuplicate(self, nums):

        numset = set()
        for i in nums:
            if i in numset:
                return True
            numset.add(i)
        return False


"""
Sort then solve solution:
time complexity:    O(NlogN)
space complexity:   O(1)
"""
class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for j in range(len(nums)-1):
            if nums[j]==nums[j+1]: return True
        return False


"""
Brute force solution:
time complexity:    O(N^2)
space complexity:   O(1)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]: return True
        return False
