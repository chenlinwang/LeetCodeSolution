import java.util.ArrayDeque;

/*
 * @lc app=leetcode id=4 lang=java
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (25.37%)
 * Total Accepted:    376.8K
 * Total Submissions: 1.5M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * 
 * Find the median of the two sorted arrays. The overall run time complexity
 * should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 * 
 * Example 1:
 * 
 * 
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * The median is 2.0
 * 
 * 
 * Example 2:
 * 
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * The median is (2 + 3)/2 = 2.5
 * 
 * 
 */
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
       ArrayDeque<Integer> mergeQue = new ArrayDeque<>();
       int totalLength = (nums1.length + nums2.length), medianLength = totalLength / 2;

       int idx = 0, idx1 = 0, idx2 = 0;
       boolean nextIsNums1 = true;
       while (idx <= medianLength) {
          if (idx1 < nums1.length && idx2 < nums2.length) {
              nextIsNums1 = nums1[idx1] < nums2[idx2];
              mergeQue.addFirst(Integer.valueOf(nextIsNums1?nums1[idx1]:nums2[idx2]));
          } else if (idx2 == nums2.length) {
              nextIsNums1 = true;
              mergeQue.addFirst(Integer.valueOf(nums1[idx1]));
          } else if (idx1 == nums1.length) {
              nextIsNums1 = false;
              mergeQue.addFirst(Integer.valueOf(nums2[idx2]));
          }

          if (nextIsNums1) {
              idx1 += 1;
          } else {
              idx2 += 1;
          }
          idx += 1;
       }
       
       System.out.format("Queue: %s\n", mergeQue);
       if (medianLength*2 == totalLength) {
           return ((double) mergeQue.pollFirst() + mergeQue.pollFirst()) / 2.0;
       } else {
           return (double) mergeQue.pollFirst();
       }
    }
}
