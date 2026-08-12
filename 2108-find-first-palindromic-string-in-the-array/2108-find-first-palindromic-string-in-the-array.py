class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            left = 0
            right = len(word) - 1
            while left <= right:
                if word[left] != word[right]:
                    break
                left += 1
                right -= 1
            else:      
                return word
        return ""

# for i in range(len(words)):
#             if words[i]==words[i][::-1]:
#                 return words[i]
#         else:
#             return ""     