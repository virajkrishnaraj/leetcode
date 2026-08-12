class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0
        for sentence in sentences:
            words = sentence.split()
            words_length = len(words)
            
            if words_length > max:
                max = words_length
                
        return max
        