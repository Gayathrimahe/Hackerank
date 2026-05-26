from typing import List
def find_LIS(nums : List[int]) -> int :
    tails = []
    for num in nums:
        lo, hi = 0 , len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            
            if tails[mid] < num:
                lo = mid + 1
            else:
                hi = mid
                
        if lo == len(tails):
            tails.append(num)
        else:
            tails[lo] = num
    return print(len(tails))

find_LIS([10,2,4,6,3,8])      
        
            
