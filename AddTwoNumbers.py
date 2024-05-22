def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        node = newList
        C = 0
        
        while l1 is not None or l2 is not None or C != 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            print (x,y)
            sum = x+y+C
            C = sum//10
            
            node.next = ListNode(sum%10)
            node = node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        print (newList)
        result = newList.next
        newList.next = None
        return result