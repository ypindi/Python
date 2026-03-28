# 392. Is Subsequence Solved Easy Topics premium lock icon 
# Companies Given two strings s and t, return true if s is 
# a subsequence of t, or false otherwise. A subsequence of 
# a string is a new string that is formed from the 
# original string by deleting some (can be none) of the 
# characters without disturbing the relative positions of 
# the remaining characters. (i.e., "ace" is a subsequence 
# of "abcde" while "aec" is not). 

# Example 1: Input: s = "abc", t = "ahbgdc" 
# Output: true 
# Example 2: Input: s = "axc", t = "ahbgdc" 
# Output: false 

# Constraints: 0 <= s.length <= 100 
# 0 <= t.length <= 104 
# s and t consist only of lowercase English letters. 

# Follow up: Suppose there are lots of incoming s, 
# say s1, s2, ..., sk where k >= 109, and you want to 
# check one by one to see if t has its subsequence. 
# In this scenario, how would you change your code?

# Follow up Solution:
from collections import defaultdict
import bisect

class SubsequenceChecker:
    def __init__(self, t: str):
        self.positions = defaultdict(list)
        for i, ch in enumerate(t):
            self.positions[ch].append(i)

    def isSubsequence(self, s: str) -> bool:
        prev_index = -1

        for ch in s:
            if ch not in self.positions:
                return False

            idx_list = self.positions[ch]
            next_pos = bisect.bisect_right(idx_list, prev_index)

            if next_pos == len(idx_list):
                return False

            prev_index = idx_list[next_pos]

        return True