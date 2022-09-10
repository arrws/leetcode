import bisect

def longest_inc_subseq(v):
    # O(n*log(n))
    # keep partial longest inc subseq here
    # first elements will be overwritten by shorter inc subseq
    a = []
    for x in v:
        # search for an element (at pos i-1) smaller than x
        i = bisect.bisect_left(a, x)
        # if x is greater than all elems add it and inc the subseq
        if i == len(a):
            a.append(x)
        else:
            # elem at pos i can be minimized by x
            a[i] = x
        # print(a)
    return len(a)

# print(a):
# [10, 0, 0, 0, 0, 0, 0, 0, 0]
# [10, 22, 0, 0, 0, 0, 0, 0, 0]
# [9, 22, 0, 0, 0, 0, 0, 0, 0]
# [9, 22, 33, 0, 0, 0, 0, 0, 0]
# [9, 21, 33, 0, 0, 0, 0, 0, 0]
# [9, 21, 33, 50, 0, 0, 0, 0, 0]
# [9, 21, 33, 41, 0, 0, 0, 0, 0]
# [9, 21, 33, 41, 60, 0, 0, 0, 0]
print(longest_inc_subseq([10, 22, 9, 33, 21, 50, 41, 60]))
