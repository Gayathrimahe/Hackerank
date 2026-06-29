""" Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?"""

from typing import List
##checks if the next number is greater than the current number and if it is then it adds it to the result list and then sorts the result list and returns the length of the result list. This is not the correct way to solve the problem of finding the length of the longest increasing subsequence. The correct way to solve this problem is to use dynamic programming or binary search.
#class Solution:
#    def lengthOfLIS(self, nums: List[int]) -> int:
#        result = []
#        for i in range(0,len(nums)-1):
#            if nums[i] < nums[i+1]:
#                result.append(nums[i])
#        result.sort()
#        print(result)
#        print(len(result))
#            
#
#
#nums = [67,2,4,1,6,56]
#test = Solution()
#print(test.lengthOfLIS(nums))

def lengthOfLIS(nums: List[int]) -> int:
    dp = [1] * len(nums) # initialize the length with 1 for each element
    for i in range(0, len(nums)):
        print("i: ", i, "nums[i]: ", nums[i], "dp: ", dp)
        for j in range(i):
            print("j: ", j, "nums[j]: ", nums[j], "comparing:", nums[i], ">", nums[j], "→", nums[i] > nums[j])
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                print("j: ", j, "nums[j]: ", nums[j], "dp: ", dp)
    return max(dp) if dp else 0

#nums = [67,2,4,1,6]
nums = [1,5,6,2,7,8]
print(lengthOfLIS(nums))
#print(lengthOfLIS([10,9,2,5,3,7,101,18]))
