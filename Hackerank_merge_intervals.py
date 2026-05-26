""" 
intervals = [[1,5],[1,3],[2,6]]
intervals.sort()
→ [[1,3],[1,5],[2,6]]   sorts by first AND second element
→ intervals.sort(key=lambda x: x[0])
# → [[1,5],[1,3],[2,6]]   sorts ONLY by first element, keeps original order for ties"""
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