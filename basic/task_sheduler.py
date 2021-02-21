import collections
"""
Given a char array of tasks, return the least number of intervals to finish all the given tasks.
between two same tasks there must be at least n intervals (different tasks or idle)
"""

def least_interval(tasks, n):
    # [A, A, A, B, B, B, C], 2
    f = collections.Counter(tasks)
    f = list(f.values())    # [3, 3, 1]
    mx = max(f)             # 3
    k = f.count(mx)         # 2
    intervals = (mx-1) * (n+1-k)    # [A, B, idle, A, B, idle, A, B]
    tasks_left = len(tasks) - mx*k  # 1
    return max(intervals, tasks_left) + mx*k

print(least_interval(["A","A","A","B","B","B", "C"], 2))
