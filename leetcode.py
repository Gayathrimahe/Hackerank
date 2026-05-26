#Input_arr = [1,2,5,7,8,10]
##enclose the operation in a function
#def find_missing_nums(Input_arr):
## use sort method to sort list/ array in ascending order. To remove duplicates use set
#  sorted_arr = sorted(Input_arr)
#  sort_arr = sort(Input_arr)
#  print(f"sorted_arr:{sorted_arr} , sort_arr:{sort_arr}")
#
#find_missing_nums(Input_arr = [1,2,5,7,8,10])


#Scenario 1: Generate random numbers for a given range
#def generate_random_num(n):
#    return random.sample(range(n + 1), n)  # O(n), no collision risk

#find random numbers for a given range, best case
#import random
#def find_random_num(n):
#    return random.sample(range(50),n)
#
#print(find_random_num(10))
#
##worst case (With collision risk)
##does a linear check each time, for larger range this is ineffiecient.
##consumes more CPU time and memory as n increases, especially if n is close to the range limit.
#def generate_random_num(n): 
#    data = []
#    for _ in range(n):
#        x = random.randint(0,25)
#        if x not in data:
#            data.append(x)
#    return data
#
#print(generate_random_num(10))
#
#Scenario3
# Complexity Comparison

#| Approach         | Lookup | Overall  | Collision Retries          |
#|------------------|--------|----------|----------------------------|
#| Original (list)  | O(n)   | O(n²)    | Yes, worsens over time     |
#| Set-based        | O(1)   | O(n) avg | Yes, but cheap             |
#| `random.sample`  | —      | O(n)     | None                       |
import random
def generate_random_num(n):
    data = []
    result = set()
    for _ in range(n):
        x = random.randint(0,25)
        if x not in result:
            result.add(x)
            data.append(x)
    return data