# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        mergedListHead = ListNode(0)
        mergedListTail = mergedListHead

        # Check edge cases 
        if not list1: 
            return list2
        
        if not list2: 
            return list1

        # While list1 exists, add lowest element of list1 or list2 to list
        while list1:
            #While list2 exists, merge
            if list2: 
                #If list2 val is <= list1, add list2 node
                if list2.val <= list1.val: 
                    mergedListTail.next = list2
                    mergedListTail = mergedListTail.next 
                    list2 = list2.next 
                #If list1 val is < list2, add list1 node
                else: 
                    mergedListTail.next = list1
                    mergedListTail = mergedListTail.next
                    list1 = list1.next 
            #If list2 no longer exists, add all of list1 and break 
            else: 
                mergedListTail.next = list1
                break
        
        #Once list1 is depleted, make sure list2 is empty
        if list2: 
            mergedListTail.next = list2

        return mergedListHead.next



        