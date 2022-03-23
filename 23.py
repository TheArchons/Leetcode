# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#put leetcode code here
"""class Solution:
    def mergeTwoLists(self, list1, list2): #code from 21.py
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

    def mergeKLists(self, lists):
        if not lists: #if empty list
            return None
        startList = lists[0]
        for i in range(1, len(lists)):
            if not lists[i]: #if the list is empty, skip it
                continue
            startList = self.mergeTwoLists(self, startList, lists[i])
        return startList"""

class Solution:
    def mergeKLists(self, lists):
        #skip if empty list
        if not lists:
            return None

        #put all values into an array
        array = []
        for l in lists:
            while l:
                array.append(l.val)
                l = l.next
        
        #skip if empty array
        if not array:
            return None

        #sort the array
        array.sort()

        #create a new linked list
        head = ListNode()
        prev = head
        outputList = head
        for i in range(len(array)):
            head.val = array[i]
            head.next = ListNode()
            prev = head
            head = head.next

        #remove the last node
        prev.next = None

        return outputList

#debug code

ins = input().split('],')
lists = []

for l in ins:
    list1 = l.strip('[]').split(',')
    list1 = [int(i) for i in list1]

    l1 = ListNode(list1[0])
    head = l1
    for i in range(1,len(list1)):
        head.next = ListNode(list1[i])
        head = head.next
    lists.append(l1)

result = Solution.mergeKLists(Solution, lists)

#print result
while result != None:
    print(result.val)
    result = result.next