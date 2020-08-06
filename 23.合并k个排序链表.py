#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (52.57%)
# Likes:    827
# Dislikes: 0
# Total Accepted:    152.4K
# Total Submissions: 289.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next == None:
            return '[{}]'.format(self.val)
        else:
            return '[{}]->{}'.format(self.val,self.next.__repr__())

class Solution:
    def __init__(self):        
        self.comparedQueue = None

    ## maintain a NodeList of NodeList that preserve head item order          
    def insertNodeToComparedQueue(self,headNode: ListNode):
        # print("inserting {} into {}".format(headNode,comparedQueue))
        headNode = ListNode(headNode)
        if self.comparedQueue == None:
            self.comparedQueue = headNode
        else:
            previousCompareNode = None
            iterateCompareNode = self.comparedQueue
            while iterateCompareNode.next != None:
                if headNode.val.val <= iterateCompareNode.val.val:
                    # do insert and switch
                    headNode.next = iterateCompareNode
                    if previousCompareNode == None:
                        ## it's head                        
                        self.comparedQueue = headNode
                    else:
                        previousCompareNode.next = headNode
                    break
                previousCompareNode = iterateCompareNode
                iterateCompareNode = iterateCompareNode.next             
            if headNode.next == None:
                if headNode.val.val <= iterateCompareNode.val.val:
                    headNode.next = iterateCompareNode
                    if previousCompareNode == None:
                        self.comparedQueue = headNode
                    else:
                        previousCompareNode.next = headNode
                else:
                    iterateCompareNode.next = headNode
        # print("giving {}".format(comparedQueue))        

    def mergeKLists(self, lists) -> ListNode:
        lists = list(filter(lambda n: n != None and n.val != None, lists))
        listCount = len(lists)
        mergedListNode = None
        if listCount == 0:
            return mergedListNode        
        ## get each head to inseart into the list        
        for idx in range(listCount):
            self.insertNodeToComparedQueue(lists[idx])                
        ## start iterations
        mergedListNode = ListNode(None)
        mergedListNodeTail = mergedListNode
        while self.comparedQueue != None:            
            headComparedNode = self.comparedQueue.val
            replaceHeadComparedNode = headComparedNode.next

            # inseart the node
            mergedListNodeTail.next = headComparedNode
            mergedListNodeTail = headComparedNode

            # do inseart the nodes
            self.comparedQueue = self.comparedQueue.next      
            if replaceHeadComparedNode == None:
                continue
            elif self.comparedQueue == None:
                self.comparedQueue = ListNode(replaceHeadComparedNode)
            else:
                self.insertNodeToComparedQueue(replaceHeadComparedNode)
        return mergedListNode.next

def listToListNode(l:list) -> ListNode:
    if len(l) == 0:
        return None
    else:
        head = ListNode(l[0])
        current = head
        for idx in range(1,len(l)):
            current.next = ListNode(l[idx])
            current = current.next
        return head

if __name__ == '__main__':
    lists = [
        [-8,-7,-7,-5,1,1,3,4],
        [-2],
        [-10,-7,0,1,3],
        [2]
    ]
    lists = [listToListNode(l) for l in lists]
    
    s = Solution()
    print(s.mergeKLists(lists))

# @lc code=end