class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        maxi = 0
        ones = 0
        abs_1 = 9999999999999999999999
        abs_0 = 9999999999999999999999
        for i in range(len(nums)):
            if nums[i] ^ k > nums[i]:
                ones += 1
                maxi += (nums[i] ^ k)
                abs_1 = min(abs_1, (nums[i] ^ k) - nums[i])
            else:
                maxi += nums[i]
                abs_0 = min(abs_0, - (nums[i] ^ k) + nums[i])
        
        if ones % 2 == 0:
            return maxi
        else:
            return max(maxi - abs_0, maxi - abs_1)

