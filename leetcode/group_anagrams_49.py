"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def checkAnagrams(self,str1: str,str2: str) -> bool:
        if sorted(str1)==sorted(str2):
            return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        for i,s1 in enumerate(strs):
            ana = [s1]
            for j, s2 in enumerate(strs[i+1:]):
                if self.checkAnagrams(s1,s2):
                    ana.append(s2)
                    strs.remove(s2)
            anagrams.append(ana)
        return anagrams

s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
s.groupAnagrams(strs)

# Efficient way

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in mp:
                ans[mp[sorted_str]].append(s)
            else:
                mp[sorted_str] = len(ans)
                ans.append([s])    
        return ans
     
s1 = Solution1()
strs = ["eat","tea","tan","ate","nat","bat"]
s1.groupAnagrams(strs)
