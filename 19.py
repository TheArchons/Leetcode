# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
class Solution:
    def removeNthFromEnd(self, l1, n: int):
        #find the length of the list
        head = l1
        length = 0
        while head:
            length += 1
            head = head.next
        
        #travel to the nth node minus one from the end
        head = l1
        for i in range(length - n - 1):
            head = head.next

        #remove the next node
        if head.next:
            head.next = head.next.next
        else:
            l1 = None

        return l1

#debug code
list1 = input().strip('[]').split(',')
list1 = [int(i) for i in list1]
n = int(input())

l1 = ListNode(list1[0])
head = l1
for i in range(1,len(list1)):
    head.next = ListNode(list1[i])
    head = head.next

result = Solution.removeNthFromEnd(Solution, l1, n)

#print result
while result != None:
    print(result.val)
    result = result.next