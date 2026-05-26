import sys 
from collections import defaultdict

def find_substring():
    # enter the main string from with subsegment will be found
    input_string = input().strip().lower()
    # enter the number of words in the subsegment
    k = int(input())
    search_string = set()
    for n in range(k):
        # enter the words in the subsegment
       word = input().strip().lower()
       search_string.add(word)
    
    count = defaultdict(int)
    matched_string = []
    best_match = 0
    worst_match = 0
    best    = (0, float('inf'))   
    #print(search_string)
    for item in input_string.split():
        if item in search_string and item not in matched_string:
            matched_string.append(item)
    print(' '.join(matched_string))

        #else:
            #print("NO SUBSEGMENT FOUND")


find_substring()