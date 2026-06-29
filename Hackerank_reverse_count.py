def reverse_count_string(s):
    arr = list(s)
    left = 0
    right =len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1
    print("".join(arr))
    print(arr.count('1'))
    
print(reverse_count_string("100110111101"))  # Output: 3