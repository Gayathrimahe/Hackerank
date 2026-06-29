
"""# 1. find all even numbers in a list
[x for x in nums if x % 2 == 0]

# 2. find all pairs that sum to target
[[i,j] for i in nums for j in nums if i+j == target]

# 3. flatten a 2D list
[x for row in matrix for x in row]

# 4. find all prime numbers up to n
[x for x in range(2,n) if all(x%i!=0 for i in range(2,x))]

# 5. get squares of even numbers
[x**2 for x in nums if x%2==0]

# 6. find all coordinates in 2D grid
[[i,j] for i in range(x+1) for j in range(y+1)]

# 7. filter words longer than 3 chars
[word for word in words if len(word) > 3]

# 8. remove duplicates keeping order
[x for i,x in enumerate(nums) if x not in nums[:i]]"""
def print_3d_arr(x,y,z,n):
    result = [[i,j,k]
                for i in range(x+1)
                for j in range(y+1)
                for k in range(z+1)
                if i+j+k !=n
                ]
    print(result)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print_3d_arr(x,y,z,n)