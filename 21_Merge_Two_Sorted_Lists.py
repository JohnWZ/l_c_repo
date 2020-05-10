# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
思路：
先比较两个list的head谁小，小的作为head指向大的，并且额外保存一个head用作输出
用一个循环条件同时遍历两个list，比较两个list相同位置下的两个node，先指向小的node，再指向大的node，进入下一个循环
遍历结束后返回head
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # here