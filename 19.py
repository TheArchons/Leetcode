# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""#put leetcode code here 
class Solution: #2 pass solution
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
        if length - n == 0:
            return l1.next
        else:
            head.next = head.next.next

        return l1"""

#put leetcode code here 
class Solution: #1 pass solution
    def removeNthFromEnd(self, l1, n: int):
        head1, head2 = l1, l1

        #move head1 n nodes ahead
        for i in range(n):
            head1 = head1.next

        if head1 is None:
            return l1.next

        #move head1 to the end while also moving head2
        while head1.next:
            head1 = head1.next
            head2 = head2.next
        
        #remove the node
        head2.next = head2.next.next

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