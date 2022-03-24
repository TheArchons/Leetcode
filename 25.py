# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
class Solution:
    def reverseKGroup(self, l1, k: int):
        if l1 is None or l1.next is None:
            return l1

        start = l1
        prev = l1
        curr = l1.next
        next = curr.next

        #check if the list is long enough for at least one group
        for i in range(k-1):
            if curr is None:
                return l1
            curr = curr.next
        
        l1 = curr
        curr = prev.next
        
        while True:
            #check if group is large enough'
            head = start
            for i in range(k-1):
                if head is None:
                    return l1
                head = head.next
            
            #reverse the group
            for i in range(k-1):
                curr.next = prev
                prev = curr
                curr = next
                next = next.next
            
            #if the next group is large enough, start a new group and set start to the end of the next group
            head = next
            for i in range(k-1):
                if head is None:
                    start.next = next
                    return l1
                head = head.next
            start.next = head
            start = next
        
        return l1
            


#debug code
list1 = input().strip('[]').split(',')
list1 = [int(i) for i in list1]

k = int(input())

l1 = ListNode(list1[0])
head = l1
for i in range(1,len(list1)):
    head.next = ListNode(list1[i])
    head = head.next

result = Solution.reverseKGroup(Solution, l1, k)

#print result
while result != None:
    print(result.val)
    result = result.next