class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        ans =0
        for i, ch in enumerate(s, 1):
            reverse = 123 - ord(ch)
            ans += i * reverse
        return ans
        