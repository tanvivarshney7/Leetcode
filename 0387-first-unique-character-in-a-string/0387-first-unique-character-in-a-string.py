class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        index = 0

        for char in s:
            if freq[char] == 1:
                return index
                break
            index += 1
        return -1