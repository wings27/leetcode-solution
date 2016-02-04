from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def xor():
            return lambda x, y: x ^ y
        nums_xor = reduce(xor(), nums)
        mask = nums_xor & ~(nums_xor - 1)
        return [reduce(xor(), [n for n in nums if not mask & n]),
                reduce(xor(), [n for n in nums if mask & n])]
