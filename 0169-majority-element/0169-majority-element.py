class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = {}

        for n in nums:
            if n not in values:
                values[n] = 0
            values[n] = values[n] + 1

            if values[n] > len(nums)/2:
                return n
        