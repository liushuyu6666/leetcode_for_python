class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = int((l1.val + l2.val) / 10)
        remain = (l1.val + l2.val) % 10
        ans = ListNode(remain)
        p = ans
        while(l1.next != None or l2.next != None):
            if l1.next == None:
                num1 = 0
            else:
                l1 = l1.next
                num1 = l1.val

            if l2.next == None:
                num2 = 0
            else:
                l2 = l2.next
                num2 = l2.val

            remain = (num1 + num2 + carry) % 10
            carry = int((num1 + num2 + carry) / 10)
            p.next = ListNode(remain)
            p = p.next


        if carry != 0:
            p.next = ListNode(carry)

        return ans




if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(8, ListNode(9))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()

    def printListNode(l: ListNode):
        print(l.val)
        while(l.next != None):
            l = l.next
            print(l.val)

    printListNode(s.addTwoNumbers(l1, l2))