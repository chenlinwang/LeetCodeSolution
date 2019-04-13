#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.37%)
# Total Accepted:    376.8K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
import math
class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        len1 = len(nums1)
        len2 = len(nums2)
        totalLength = len1 + len2
        medianIdx = math.floor(totalLength/2)

        popedIndex = 0
        breakFlag = False
        while popedIndex < (medianIdx - 1):
            if len(nums1) > 0:
                num1 = nums1.pop()
            else:
                breakFlag = True
                nums1 = nums2
                nums2 = []
                break
            if len(nums2) > 0:
                num2 = nums2.pop()
            else:
                nums1.append(num1)
                breakFlag = True
                break

            if num1 > num2:
                nums2.append(num2)
            else:
                nums1.append(num1)
            popedIndex += 1

        # carry on
        if breakFlag == True:
            while popedIndex < (medianIdx - 1):
                nums1.pop()
                popedIndex += 1

        if len(nums2) > len(nums1):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp

        print(nums1,nums2)
        if len(nums1) == 1 and len(nums2) == 0:
            return nums1.pop()

        lastList = []
        lastList.append(nums1.pop())
        num = nums1.pop() if len(nums2) == 0 else nums2.pop()
        lastList.append(num)

        if len(nums1) != 0:
            lastList.append(nums1.pop())
        if len(nums2) != 0:
            lastList.append(nums2.pop())

        lastList.sort()
        print(lastList)
        # middle check
        if medianIdx * 2 == totalLength:
            return (lastList.pop() + lastList.pop()) / 2
        else:
            lastList.pop()
            return lastList.pop()
