# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast = slow = head

        # Find the mid
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None


        curr = head2
        prev = None
        #Reverse the second half
        while curr!=None:
            temp=curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev

        first = head
        second = head2


        flag = True

        #Check if palindrome
        while first!=None and second!=None:
            if first.val!=second.val:
                flag = False
                break
            first = first.next
            second = second.next
        
        return flag
            


            
        