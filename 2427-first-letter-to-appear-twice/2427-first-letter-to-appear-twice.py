class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        value = ''
        for char in s:
            value = char
            if char in dict:
                return char
            dict[char] = 1
        