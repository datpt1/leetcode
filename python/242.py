"""
* 242. Valid Anagram
* Easy

Share
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        return all(s.count(c) == t.count(c) for c in "abcdefghijklmnopqrstuvwxyz")

if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
