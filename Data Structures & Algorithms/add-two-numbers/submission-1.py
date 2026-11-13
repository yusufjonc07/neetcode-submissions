# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        res = ListNode(0)
        ptr = res

        firstNum = ""
        while l1:
            firstNum = str(l1.val) + firstNum
            l1 = l1.next

        secNum = ""
        while l2:
            secNum = str(l2.val) + secNum
            l2 = l2.next


        answ = int(firstNum)+int(secNum)

        for s in str(answ)[::-1]:
            ptr.next = ListNode(int(s))
            ptr = ptr.next

        
        return res.next
        # def remain(ptr, l1, l2):
            
        #     if not l1 or not l2:
        #         return 0, ptr

        #     val1, val2 = l1.val, l2.val

        #     l1, l2 = l1.next, l2.next

        #     lastrem, node = remain(ptr, l1, l2)
        #     ptr.next = ListNode((val1+val2)%10)
        #     ptr = ptr.next

        #     return lastrem, ptr

        # lastrem, ptr = remain(ptr, l1, l2)

        # return res


        

