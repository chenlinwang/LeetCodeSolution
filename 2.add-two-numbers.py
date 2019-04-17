#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.92%)
# Total Accepted:    830.7K
# Total Submissions: 2.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2,l1,l2 = self.getValue(l1,l2)
        total, previousRemain = self.refine(num1+num2)
        result = ListNode(total)
        node = result
        while (l1 != None and l2 != None):
            num1,num2,l1,l2 = self.getValue(l1,l2)
            total, previousRemain = self.refine(num1+num2+previousRemain)
            newNode = ListNode(total)
            node.next = newNode
            node = newNode
        
        if (l1 != None):
            node.next=l1
            self.addOn(l1,previousRemain)
        elif (l2 != None):
            node.next=l2
            self.addOn(l2,previousRemain)
        elif (previousRemain > 0):
            node.next = ListNode(previousRemain)

        return result
        
    def getValue(self, l1: ListNode, l2: ListNode):
        return l1.val,l2.val,l1.next,l2.next

    def refine(self,s: int):
        if s < 10:
            return s,0
        else:
            return s-10,1

    def addOn(self, l: ListNode, previousRemain: int):
        while(previousRemain > 0 and l.next != None):
            total, previousRemain = self.refine(l.val+previousRemain)
            l.val = total
            l = l.next
        
        total,previousRemain = self.refine(l.val+previousRemain)
        l.val = total
        if (previousRemain > 0):
            l.next = ListNode(previousRemain)