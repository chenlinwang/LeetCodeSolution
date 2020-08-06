#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (32.82%)
# Likes:    1141
# Dislikes: 3484
# Total Accepted:    346.7K
# Total Submissions: 1.1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:
    # 83.78 / 10
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            r = ""
            lenR = len(s)
            d = 2*numRows - 2
            for jdx in range(0,lenR,d):
                r += s[jdx]

            for idx in range(1,numRows-1):
                for jdx in range(idx,lenR,d):
                    kdx = jdx - 2 * idx + d
                    if kdx < lenR:
                        r += s[jdx]+s[kdx]
                    else:
                        r += s[jdx]

            for jdx in range(numRows-1,lenR,d):
                r += s[jdx]
            return r
        
