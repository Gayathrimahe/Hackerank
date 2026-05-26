#def find_max_subarr_sum(arr):
#    max_sum = arr[0]
#    curr_sum = arr[0]
#    print(f"Initial max_sum: {max_sum}, curr_sum: {curr_sum}")
#    for i in range(len(arr)):
#        print(f"Current index: {i}, Current element: {arr[i]}")
#        curr_sum = max(arr[i],curr_sum + arr[i])
#        print(f"Updated curr_sum: {curr_sum}, max_sum: {max_sum}")
#        max_sum = max(max_sum, curr_sum)
#    return max_sum
#
#print(find_max_subarr_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6


#find maximum subarray sum using divide and conquer approach
def max_subarray_sum(arr):
    curr_arr = arr[0]
    max_arr =arr[0]
    for i in range(1,len(arr)):
        curr_arr = max(arr[i],curr_arr + arr[i])
        max_arr = max(max_arr , curr_arr)
        print(f"Current index: {i}, Current element: {arr[i]}, Current subarray sum: {curr_arr}, Maximum subarray sum so far: {max_arr}")
    return max_arr

print(max_subarray_sum( [1, 2, 3, -2, 5]))  # Output: 6