class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        return str(x) in str(n) and not str(n).startswith(str(x))
        