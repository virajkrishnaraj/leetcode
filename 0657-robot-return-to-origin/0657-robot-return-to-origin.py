class Solution(object):
    def judgeCircle(self, moves):
        counts = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for ch in moves:
            counts[ch] += 1
        
        if counts["L"] == counts["R"] and counts["U"] == counts["D"]:
            return True
        else:
            return False 
        