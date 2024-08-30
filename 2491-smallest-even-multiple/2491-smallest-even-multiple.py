class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        while(n >=1 and n <= 150):
            if n%2==0:
                return n
            else:
                return (n*2)