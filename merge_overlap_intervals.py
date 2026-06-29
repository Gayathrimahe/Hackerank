"""DIRECT MATCHES — same merge logic:
────────────────────────────────────────────
1. Merge Intervals              LC 56
   input: [[1,3],[2,6],[8,10]]
   output: [[1,6],[8,10]]

2. Employee Free Time           LC 759
   input: schedules as intervals
   output: free time intervals

3. Merge Two Sorted Intervals   HackerRank
   input: two lists of intervals
   output: merged sorted list

USES SAME SORT + SCAN PATTERN:
────────────────────────────────────────────
4. Meeting Rooms                LC 252
   can one person attend all meetings?

5. Meeting Rooms II             LC 253
   minimum rooms needed

6. Non Overlapping Intervals    LC 435
   minimum removals to make non overlapping

7. Insert Interval              LC 57
   insert new interval and merge

INPUT FORMAT VARIATIONS:
────────────────────────────────────────────
8. starts and ends given separately
   n=3
   start=[1,2,8]
   end=[3,6,10]
   → your exact code handles this ✅

9. pairs given as one flat list
   [1,3,2,6,8,10]
   → intervals=[[nums[i],nums[i+1]]
                for i in range(0,len(nums),2)]

10. each pair on separate line
    1 3
    2 6
    8 10
    → intervals=[[int(x) for x in input().split()]
                 for _ in range(n)]

    Returns:
        _type_: _description_
    """
   

n = 3
start = [1, 2, 8]
end = [3, 6, 10]

def merged(start, end, n):
    
    # WAY 1 — traditional for loop
    # manually pick start[i] and end[i] at same index
    # most readable for beginners
    intervals = []
    for i in range(n):
        intervals.append([start[i], end[i]])
    print(f"for loop        : {intervals}")
    # → [[1,3],[2,6],[8,10]]

    # WAY 2 — list comprehension
    # same as way 1 but one line
    # pythonic and cleaner
    small_intervals = [[start[i], end[i]] for i in range(n)]
    print(f"list comprehension: {small_intervals}")
    # → [[1,3],[2,6],[8,10]]

    # WAY 3 — zip
    # zip pairs elements at same index automatically
    # no index needed, cleanest approach
    zipped_intervals = [list(pair) for pair in zip(start, end)]
    print(f"zip             : {zipped_intervals}")
    # → [[1,3],[2,6],[8,10]]

    # ALWAYS SORT — never assume input is sorted
    # sort by start time (index 0)
    # example: start=[2,1,8] would give wrong merge without sorting
    intervals.sort(key=lambda x: x[0])
    print(f"after sort      : {intervals}")

    # MERGE — walk through sorted intervals
    # two cases:
    # 1. no overlap → gap exists → just append
    # 2. overlap exists → extend end of last interval
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            # not merged → list empty, nothing to compare
            # merged[-1][1] < interval[0] → last end < current start → no overlap
            merged.append(interval)
        else:
            # overlap → extend end to cover both intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

result = merged(start, end, n)
print(f"merged intervals: {result}")