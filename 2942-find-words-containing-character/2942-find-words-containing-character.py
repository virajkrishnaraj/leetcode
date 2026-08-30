class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for index in range(len(words)):
            if x in words[index]:
                result.append(index)
        return result



                
        