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

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> numset;
        for(int num:nums){
            if(numset.find(num)!=numset.end())
                return true;
            numset.insert(num);
        }
        return false;
        
    }
};

