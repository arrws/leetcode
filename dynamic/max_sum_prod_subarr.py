def max_subarr(v):
    maxs = max(v)
    start = stop = v.index(maxs)
    s = 0
    j = 0
    for i, x in enumerate(v):
        if s < 0:
            s = x
            j = i
        else:
            s += x
        if s > maxs:
            maxs = s
            start = j
            stop = i
    print(maxs, v[start:stop+1])

def max_kadane(v):
    here = sofar = v[0]
    for x in v[1:]:
        here = max(x, here+x)
        sofar = max(sofar, here)
    print(sofar)

max_subarr([-2, -3, 4, -1, -2, 1, 5, -3])
max_kadane([-2, -3, 4, -1, -2, 1, 5, -3])


def max_subarr_prod(v):
    p = v[0]
    mx = v[0]
    mn = v[0]
    for x in v[1:]:
        a = [x, mx*x, mn*x]
        mx = max(a)
        mn = min(a)
        p = max(p, mx)
    print(p)

max_subarr_prod([1, 2, -1, 0, 20, -1, -3, 0, 7, 8, -2])

