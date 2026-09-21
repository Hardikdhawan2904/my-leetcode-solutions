class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = [0] * k
        dp = [0]*k
        for i in nums:
            rem = i % k
            new_dp=[0]*k
            new_dp[rem] += 1
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * rem) % k
                    new_dp[new_r] += dp[r]
            
            dp = new_dp
            for r in range(k):
                results[r] += dp[r]
        
        return results