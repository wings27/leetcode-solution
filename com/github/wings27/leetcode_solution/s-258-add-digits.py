class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        reminder = num % 9
        return 9 if (reminder == 0 and num != 0) else reminder
