class Solution(object):
    def xorOperation(self, n, start):
        ans = 0
        for i in range(0, n):
            ans ^= start + 2 * i

        return ans



# nums = [0] * n
# for i in range(n):
#     nums[i] = start + 2 * i

# ans = 0
# for num in nums:
#     ans ^= num

# return ans