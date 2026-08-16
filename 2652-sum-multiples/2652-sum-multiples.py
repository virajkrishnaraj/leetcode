class Solution(object):
    def sumOfMultiples(self, n):
        my_list = []
        for i in range(1, n+1):
            if i%3==0 or i%5==0 or i%7==0:
                my_list.append(i)
        return sum(my_list)

        