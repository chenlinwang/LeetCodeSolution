#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.71%)
# Likes:    4069
# Dislikes: 377
# Total Accepted:    619.9K
# Total Submissions: 2.2M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
import math,time

class Solution:
    # ## 5.02 / 22.69
    # def longestPalindrome(self, s: str) -> str:
    #     sLength = len(s)
    #     if sLength == 0:
    #         return ""
    #     longest = 1
    #     longestStr = s[0]
    #     for idx in range(sLength):
    #         for jdx in range(sLength-1, idx + longest-1,-1):
    #             isPalindromic = True
    #             currentLength = jdx - idx + 1
    #             middle = idx + math.floor(currentLength/2)
    #             oddEven = (currentLength + 1) % 2 
    #             for dx in range(0, math.ceil(currentLength/4)):
    #                 if s[idx+dx] != s[jdx-dx] or s[middle+dx] != s[middle-dx-oddEven]:
    #                     isPalindromic = False
    #                     break
    #             if isPalindromic:
    #                 longest = currentLength
    #                 longestStr = s[idx:jdx+1]
    #                 break
    #         if longest >= (sLength - idx):
    #             break
    #     return longestStr

    ## 91.65 / 22.69
    def longestPalindrome(self, s: str) -> str:
        sLength = len(s)
        if sLength == 0:
            return ""
        middle = math.floor(sLength/2)
        longestStr = s[middle]
        for idx in range(sLength):
            if (sLength-idx)*2 <= len(longestStr):
                break
            ## as actual middle
            jdx = 1
            maxLen = min([idx,sLength-idx-1])
            if jdx <= maxLen:
                while s[idx-jdx] == s[idx+jdx]:
                    jdx += 1
                    if jdx > maxLen:
                        break
                if (jdx*2 - 1) > len(longestStr):
                    longestStr = s[idx - jdx + 1: idx + jdx]

            ## as double middle
            jdx = 1
            maxLen = min([idx+1,sLength-idx-1])
            if jdx <= maxLen:
                while s[idx-jdx+1] == s[idx+jdx]:
                    jdx += 1
                    if jdx > maxLen:
                        break
                if (jdx-1) * 2 > len(longestStr):
                    longestStr = s[idx - jdx + 2: idx + jdx]
        return longestStr

