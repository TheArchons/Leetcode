# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
class Solution:
    def isPalindrome(self, l1) -> bool:
        #get length of l1
        length = 0
        head = l1
        while head:
            length += 1
            head = head.next
        
        if length % 2 != 0: #odd
            head2Pos = length // 2 + 1
        else:
            head2Pos = length // 2
        
        head2 = l1 #travel to the middle
        for i in range(head2Pos):
            head2 = head2.next
        
        #reverse the second half
        prev = None
        curr = head2
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        #compare the first half and the second half
        head1 = l1
        while prev:
            if prev.val != head1.val:
                return False
            prev = prev.next
            head1 = head1.next
        return True

#debug code
list1 = input().strip('[]').split(',')
list1 = [int(i) for i in list1]

l1 = ListNode(list1[0])
head = l1
for i in range(1,len(list1)):
    head.next = ListNode(list1[i])
    head = head.next

result = Solution.isPalindrome(Solution, l1)

#print result
print(result)