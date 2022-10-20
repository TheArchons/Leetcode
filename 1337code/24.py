# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        next = curr.next
        head = curr
        while next and next.next:
            prev.next = next.next
            curr.next = prev
            prev = next
            curr = prev.next
            next = curr.next
        curr.next = prev
        prev.next = next
        return head

#debug code
list1 = input().strip('[]').split(',')
list1 = [int(i) for i in list1]

l1 = ListNode(list1[0])
head = l1
for i in range(1,len(list1)):
    head.next = ListNode(list1[i])
    head = head.next

result = Solution.swapPairs(Solution, l1)

#print result
while result != None:
    print(result.val)
    result = result.next