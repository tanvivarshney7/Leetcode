class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        text = str(x)
        if text == text[::-1]:
            return True
        return False