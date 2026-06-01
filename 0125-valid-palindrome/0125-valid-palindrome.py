class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += char

        cleaned = new_string.lower()

        return cleaned == cleaned[::-1]