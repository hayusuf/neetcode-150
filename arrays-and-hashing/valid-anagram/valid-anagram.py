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

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters, tletters = {}, {}

        for i in range(len(s)):
            sletters[s[i]] = 1 + sletters.get(s[i], 0)
        for i in range(len(t)):
            tletters[t[i]] = 1 + tletters.get(t[i], 0)
        return sletters == tletters


"""
Alternate solution:
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


