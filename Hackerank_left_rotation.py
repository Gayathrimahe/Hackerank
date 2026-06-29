import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    print(d, arr)
    return arr[d:] + arr[:d]
print(rotateLeft(4, [1, 2, 3, 4, 5]))  # Output: [5, 1, 2, 3, 4]