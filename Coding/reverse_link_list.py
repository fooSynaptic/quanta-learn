#py3

class Solution():
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next	#fast point move 2 step
            rev = slow
            rev.next = rev	        #rev stay in the prev node of slow and make the 
                                    #first part reversed, brilliant!
            slow = slow.next	    #slow pointer move 1 step


        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:  #compare rev and slow.next for palindrme check
            slow = slow.next
            rev = rev.next
        return not rev