# Definition for singly-linked list.
from statistics import harmonic_mean


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
"""class Solution: #O(n) time, O(n) space
    def hasCycle(self, head) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False"""

class Solution:
    def hasCycle(self, head) -> bool: #tortoise and hare algorithm
        if not head or not head.next:
            return False

        tortoise, hare = head, head.next
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False

#debug code
list1 = input().strip('[]').split(',')
list1 = [int(i) for i in list1]

l1 = ListNode(list1[0])
head = l1
prev = l1
for i in range(1,len(list1)):
    head.next = ListNode(list1[i])
    head = head.next

pos = int(input())
if pos != -1:
    end = head
    head = l1
    #travel to pos
    for i in range(pos):
        head = head.next
    end.next = head

result = Solution.hasCycle(Solution, l1)

#print result
print(result)