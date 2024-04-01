class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next :
            if cur.val==cur.next.val:
                temp=cur.next.next
                cur.next=temp
            else:
                cur=cur.next
        return head