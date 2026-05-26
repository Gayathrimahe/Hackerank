
def longestPalindrome(s):
    result = ""
    for i in range(len(s)):
        left, right = i, i
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1 
            right += 1
        odd = s[left+1:right]
        
        left, right = i, i+1
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1 
            right += 1 
        even = s[left+1 : right]
        
        if len(odd) > len(result):
            result = odd
        elif len(even) > len(result):
            result = even 
    return print(result)
    
print(longestPalindrome("madam"))