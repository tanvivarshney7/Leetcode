class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = list(set(nums))
        if len(distinct_nums) < 3:
            return max(distinct_nums)
        else:
            distinct_nums.sort(reverse=True)
            return distinct_nums[2]