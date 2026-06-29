from typing import List
def two_sum(nums : List[int], target : int):
    left = 0
    right = len(nums)-1
    index_pos = []
    while left < right:
        sum= nums[left] + nums[right]
        if (sum == target):
            
            index_pos.append([left+1, right+1])
            left = left + 1
            right = right - 1
        elif sum < target:
            left = left + 1 
        else:
            right = right - 1 
    return index_pos
print(two_sum(nums = [2,3,5,6], target = 8))
