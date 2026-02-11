class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        n = len(nums)

        for i in range(n):
            seen = set()
            target = -nums[i]

            for j in range(i + 1, n):
                need = target - nums[j]

                if need in seen:
                    triplet = tuple(sorted([nums[i], nums[j], need]))
                    res.add(triplet)
                else:
                    seen.add(nums[j])

        return list(res)
