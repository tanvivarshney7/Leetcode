class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        for ch in set(word):
            if ch.islower() and ch.upper() in word:
                count += 1
        return count
        