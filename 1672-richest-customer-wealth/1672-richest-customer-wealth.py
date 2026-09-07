class Solution(object):
    def maximumWealth(self, accounts):
        rich = 0
        for wealth in accounts:
            rich = max(rich, sum(wealth))
        return rich
        