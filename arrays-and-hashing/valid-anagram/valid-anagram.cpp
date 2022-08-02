"""
Valid Anagram
- solved using two maps 
- iterated through letters of each string and
  incremented the number of times that letter appeared,
  then returned the equal comparison operation between the two maps. 
  hashset.

time complexity:    O(N)
space complexity:   O(N)
"""

class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> sletters;
        map<char, int> tletters;
        for(char i:s){
            sletters[i]++;
        }
        for(char i:t){
            tletters[i]++;
        }
        return sletters == tletters;
        
    }
};
