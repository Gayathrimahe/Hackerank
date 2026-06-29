startTime = [1, 2, 4, 6]
endTime = [3, 5, 7, 9]
n=4
intervals = sorted(zip(startTime, endTime), key=lambda x: x[0])
print(intervals)
result = []
for i in range(n):
    for j in range(i+1, n):
        s1,e1 = intervals[i]
        s2,e2 = intervals[j]
        print(f"Checking intervals: ({s1}, {e1}) and ({s2}, {e2})")
        start = max(s1, s2)
        end = min(e1, e2)
        print(f"Overlap: ({start}, {end})")
        if start < end:
            result.append((start, end))

print(result)