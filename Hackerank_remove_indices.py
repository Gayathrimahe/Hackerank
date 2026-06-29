#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def getRemovableIndices(str1, str2):
    # Write your code here
    result = []
    
    for i in range(len(str1)):
        # remove character at index i and check if it matches str2
        modified = str1[:i] + str1[i+1:]   
        print(f"Removing index {i}:str1[{i}]={str1[i]} , str1[i+1] = {str1[i+1]} {modified} (original: {str1})")
        
        if modified == str2:
            result.append(i)
    
    return result if result else [-1]

print(getRemovableIndices("abcde", "abde"))  # Output: [2]