import bisect

def fast_longest_increasing_subseq(v):
    # O(n*log(n))
    a = [0 for _ in range(len(v)+1)]
    l = 0
    for x in v:
        f = bisect.bisect_left(a, x, 0, l)
        a[f] = x
        if f == l: # didn't find < a[l]
            l += 1
    # a is not the sequence !!
    print(l)

# print(a):
# [10, 0, 0, 0, 0, 0, 0, 0, 0]
# [10, 22, 0, 0, 0, 0, 0, 0, 0]
# [9, 22, 0, 0, 0, 0, 0, 0, 0]
# [9, 22, 33, 0, 0, 0, 0, 0, 0]
# [9, 21, 33, 0, 0, 0, 0, 0, 0]
# [9, 21, 33, 50, 0, 0, 0, 0, 0]
# [9, 21, 33, 41, 0, 0, 0, 0, 0]
# [9, 21, 33, 41, 60, 0, 0, 0, 0]
fast_longest_increasing_subseq([10, 22, 9, 33, 21, 50, 41, 60])
