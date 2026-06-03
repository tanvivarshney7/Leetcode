class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sort = sorted(nums)
        smallest_sum = 0
        for i in range(k):
            smallest_sum += sort[i]
        largest_sum = 0
        for i in range(len(nums)-k, len(nums)):
            largest_sum += sort[i]
        return abs(largest_sum - smallest_sum)