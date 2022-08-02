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

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashmap;

        for(int i = 0; i < nums.size(); i++){
            if(hashmap.find(target-nums[i]) != hashmap.end())
               return {i, hashmap[target-nums[i]]};
            hashmap.insert({nums[i], i});
        }
        return {};
    }
};
