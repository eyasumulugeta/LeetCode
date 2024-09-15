class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums:
            count = 0
            for i in range(0, len(nums)):
                if n > nums[i]:
                    count += 1
            result.append(count)
        return result