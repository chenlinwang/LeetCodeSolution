#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (26.46%)
# Total Accepted:    753.7K
# Total Submissions: 2.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        maxLength = 0
        substringList = []
        for c in s:
            # test c is in the substringList
            length = len(substringList)
            for idx in range(length):
                if substringList[idx] == c:
                    if idx == length:
                        substringList = []
                    else:
                        substringList = substringList[idx+1:]
                    break
            substringList.append(c)
            maxLength = max([maxLength,len(substringList)])
        return maxLength
        
