class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        length = len(operations)

        for i in range(0, length):
            if((operations[i] == "--X") or (operations[i] == "X--")):
                X-=1
            else:
                X+=1
        return X