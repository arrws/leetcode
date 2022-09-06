import collections
"""
Given a char array of tasks, return the least number of intervals to finish all the given tasks.
between two same tasks there must be at least n intervals (different tasks or idle)
"""

def least_interval(tasks, interval):
    # [A, A, A, B, B, B, C], 2
    freq = collections.Counter(tasks)   # {A:3, B:3, C:1}
    freq = list(freq.values())          # [3, 3, 1]

    # compute tasks that will be part of most cycle
    num_cycles = max(freq)              # 3
    k = freq.count(num_cycles)          # num longest cycles ~ 2
    num_idles = (num_cycles - 1) * (interval + 1 - k)   # [A, B, idle, A, B, idle, A, B]
    #            num of pauses   *  diff between requested num idles and my longes cycles

    # fill idles with leftover tasks
    tasks_left = len(tasks) - num_cycles * k    # num tasks not part of every cycle ~ 1

    return max(num_idles, tasks_left) + num_cycles * k

print(least_interval(["A","A","A","B","B","B", "C"], 2))
