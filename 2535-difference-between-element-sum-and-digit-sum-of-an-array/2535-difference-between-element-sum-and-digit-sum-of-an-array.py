class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for digit in str(num):
                digit_sum += int(digit)
        result = abs(element_sum - digit_sum)
        return result