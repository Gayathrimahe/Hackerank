""" 
intervals = [[1,5],[1,3],[2,6]]
intervals.sort()
→ [[1,3],[1,5],[2,6]]   sorts by first AND second element
→ intervals.sort(key=lambda x: x[0])
# → [[1,5],[1,3],[2,6]]   sorts ONLY by first element, keeps original order for ties
# 
ALGORITHM: Merge Intervals (Greedy Approach)
    ============================================
    
    WHAT IT DOES:
    -------------
    Takes a list of intervals and merges all overlapping intervals
    into the minimum number of non-overlapping intervals.
    
    HOW IT WORKS:
    -------------
    Step 1 - Sort intervals by start time
             [[1,3],[5,7],[2,4],[6,8]] → [[1,3],[2,4],[5,7],[6,8]]
    
    Step 2 - Walk through sorted intervals one by one:
             a) If merged is empty OR current start > last end
                → no overlap → append as new interval
             b) Else
                → overlap exists → extend last interval's end
    
    EXAMPLE:
    --------
    Input:  [[1,3],[2,6],[8,10],[15,18]]
    
    [1,3] → merged=[[1,3]]
    [2,6] → 3>2 overlap  → merged=[[1,6]]
    [8,10]→ 6<8 no overlap → merged=[[1,6],[8,10]]
    [15,18]→ 10<15 no overlap → merged=[[1,6],[8,10],[15,18]]
    
    Output: [[1,6],[8,10],[15,18]]
    
    TIME COMPLEXITY:
    ----------------
    O(n log n) — dominated by sorting step
    O(n)       — single pass through intervals after sort
    Overall    → O(n log n)
    
    n = number of intervals
    
    SPACE COMPLEXITY:
    -----------------
    O(n) — merged list stores at most n intervals
           in worst case no intervals overlap
           every interval gets stored separately
    O(log n) — sorting uses log n stack space internally
    Overall  → O(n)
    
    WHEN TO USE:
    ------------
    - Calendar/meeting room problems
    - Finding overlapping time slots
    - Merging ranges in any sorted data
    
    EDGE CASES:
    -----------
    - Single interval          → return as is
    - No overlaps              → return all intervals unchanged
    - All overlapping          → return one merged interval
    - Same start different end → [[1,5],[1,3]] → [[1,5]]
    
    INTERVIEW TALKING POINTS:
    -------------------------
    - Always sort first by start time — greedy choice
    - merged[-1][1] tracks end of last merged interval
    - max() handles case where one interval fully contains another
      ex: [1,10] and [2,5] → end stays 10 not 5
    """
def merge_intervals(intervals):
    intervals.sort(key = lambda x : x[0])
    merged = []
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])
            
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))