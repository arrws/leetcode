# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

def insert_interval(v, x):
    v.append(x)
    v.sort(key=lambda x: x[0])
    f = []
    for x in v:
        if len(f)<1:
            f.append(x)
        else:
            if f[-1][1] >= x[0]:
                if x[1] > f[-1][1]:
                    # merge interval
                    f[-1][1] = x[1]
                # else: skip interval
            else:
                # add new interval
                f.append(x)
    return f

def num_overlap_intervals(v):
        v.sort(key=lambda x: x[0])
        last = v[0][1]
        k = 0
        for x in v[1:]:
            if x[0] >= last:
                last = x[1]
            else:
                k += 1
                if x[1] <= last:
                    last = x[1]
        return k

def merge_intervals(v):
        v.sort(key=lambda x: x[0])

        # inplace
        j = 0
        i = 1
        while i < len(v):
            if v[j][1] < v[i][0]:
                j += 1
                i += 1
            else:
                v[j][1] = max(v[j][1], v[i][1])
                del v[i]
        return v

        # queue
        q = [v[0]]
        for i in range(1, len(v)):
            if q[-1][1] < v[i][0]:
                q.append(v[i])
            else:
                q[-1][1] = max(q[-1][1], v[i][1])
        return q

def intervalIntersection(A: List[List[int]], B: List[List[int]]):
    # Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
    # Return the intersection of these two interval lists.
    i, j = 0, 0
    r = []
    while i < len(A) and j < len(B):
        a = max(A[i][0], B[j][0])
        b = min(A[i][1], B[j][1])
        if a<=b:
            r.append([a, b])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return r

print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8] ))

