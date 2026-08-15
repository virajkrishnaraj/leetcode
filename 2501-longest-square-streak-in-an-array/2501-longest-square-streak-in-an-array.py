class Solution(object):
    def longestSquareStreak(self, nums):
        num_set = set(nums)
        max_streak = -1

        for num in num_set:
            streak = 0
            curr = num

            while curr in num_set:
                streak += 1
                curr = curr * curr

            if streak >= 2:
                max_streak = max(max_streak, streak)

        return max_streak
        