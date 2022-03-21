#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def carry(self, l1, pos): #carry the 1 to the next node
        for i in range(pos-1):
            l1 = l1.next
        l1.val += 1
        if l1.val >= 10:
            l1.val -= 10
            self.carry(l1, pos)

    def addTwoNumbers(self, l1, l2):
        l1Head = l1
        l2Head = l2
        pos = 0

        #add the first node
        l1.val += l2.val

        while l2Head.next != None: #add the rest of the nodes
            pos += 1
            l2Head = l2Head.next
            l1Head = l1Head.next
            if l1Head == None:
                l1Head = ListNode(l2Head.val)
                l1Head.next = None
            else:
                l1Head.val += l2Head.val
                if l1Head.val >= 10:
                    l1Head.val -= 10
                    self.carry(l1, pos) #carry the 1 to the next node
        
        end = l1Head #the last node
        l1Head = l1 #reset head

        #reverse
        prev = l1
        curr = l1.next
        if curr != None:
            l1Head = l1.next.next
        else:
            l1Head = None
        prev.next = None
        while curr != None:
            curr.next = prev
            prev = curr
            curr = l1Head
            if l1Head != None:
                l1Head = l1Head.next

        return prev

list1 = input().strip('[]').split(',')
list2 = input().strip('[]').split(',')
l1 = ListNode(int(list1[0]))
l2 = ListNode(int(list2[0]))

for i in range(1,len(list1)):
    travel = l1
    while travel.next != None:
        travel = travel.next
    travel.next = ListNode(int(list1[i]))
    travel = travel.next

for i in range(1, len(list2)):
    head = l2
    while head.next != None:
        head = head.next
    head.next = ListNode(int(list2[i]))
    head = head.next

result = Solution().addTwoNumbers(l1, l2)
#print result
while result != None:
    print(result.val)
    result = result.next