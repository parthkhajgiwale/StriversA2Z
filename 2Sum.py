#Brute Force Method O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    result.append(i)
                    result.append(j)
        return result

#Hash Map / Dictionary O(n)
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index
#It scans the list once, and for each number checks whether the value needed to reach the target has already been seen; if yes, it immediately returns the indices of the matching pair.
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i] #see[complement] -> index of complement term as dictionary is value : index term

            seen[num] = i
