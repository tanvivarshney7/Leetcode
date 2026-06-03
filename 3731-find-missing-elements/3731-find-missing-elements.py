class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = []
        smallest = min(nums)
        largest = max(nums)
        for num in range(smallest, largest + 1):
            if num not in nums:
                missing.append(num)
        return missing