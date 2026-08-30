class Solution(object):
    def sortedSquares(self, nums):
        result = []
        for num in nums:
            result.append(num ** 2)

        return sorted(result)
        