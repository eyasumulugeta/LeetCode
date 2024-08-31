class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        values = []
        total = 0
        for i in operations:
            length = len(values)
            if i == "C" and length >= 1:
                values.pop(length-1)
            elif i == "D":
                values.append(int(values[length - 1]) * 2)
            elif i == "+" and length > 1:
                values.append(int(values[length-1]) + int(values[length - 2]))
            else:
                values.append(i)
        for i in values:
            total+= int(i)
        return total