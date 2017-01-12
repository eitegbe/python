# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        count1 = self.countNodes(headA)
        count2 = self.countNodes(headB)
        
        if count1 > count2:
            diff = count1 - count2
            return self.intersection(diff, headA, headB)
        else:
            diff = count2 - count1
            return self.intersection(diff, headB, headA)
        
    def countNodes(self, current):
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def intersection(self, diff, headA, headB):
        currentA = headA
        currentB = headB
        
        for i in xrange(diff):
            if currentA is None:
                return None
            currentA = currentA.next
        
        while currentA is not None and currentB is not None:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None
        
