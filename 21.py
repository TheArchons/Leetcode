# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
class Solution:
    def mergeTwoLists(self, list1, list2):
        l1Head = list1
        l2Head = list2
        outputList = ListNode()
        outputListHead = outputList
        while l1Head or l2Head:
            if l1Head:
                if not l2Head or l1Head.val <= l2Head.val:
                    outputListHead.val = l1Head.val
                    outputListHead.next = ListNode()
                    outputListHead = outputListHead.next
                    l1Head = l1Head.next
                    continue
                else:
                    outputListHead.val = l2Head.val
                    outputListHead.next = ListNode()
                    outputListHead = outputListHead.next
                    l2Head = l2Head.next
                    continue
            elif l2Head:
                outputListHead.val = l2Head.val
                outputListHead.next = ListNode()
                outputListHead = outputListHead.next
                l2Head = l2Head.next
                continue

        #remove the last node
        head = outputList
        while head and head.next != outputListHead:
            head = head.next
        head.next = None
        return outputList

list1 = input().strip('[]').split(',')
list2 = input().strip('[]').split(',')
l1 = ListNode(int(list1[0]))
l2 = ListNode(int(list2[0]))

for i in range(1,len(list1)):
    head = l1
    while head.next != None:
        head = head.next
    head.next = ListNode(int(list1[i]))
    head = head.next

for i in range(1, len(list2)):
    head = l2
    while head.next != None:
        head = head.next
    head.next = ListNode(int(list2[i]))
    head = head.next

returned = Solution().mergeTwoLists(l1, l2)

while returned != None:
    print(returned.val)
    returned = returned.next