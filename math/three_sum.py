# first fit
def three_sum(v, s):
    v.sort()
    for a in range(len(v)-2):
        b = a+1
        c = len(v)-1
        while b < c:
            if v[a]+v[b]+v[c] == s:
                print(v[a],v[b],v[c])
                return
            elif v[a]+v[b]+v[c] < s:
                b += 1
            else:
                c -= 1

# all unique combinations
def all_three_sum(v, s):
        v.sort()
        r = []
        a = 0
        while a < len(v):
            b = a+1
            c = len(v)-1
            while b < c:
                if v[a]+v[b]+v[c] == s:
                    r.append([v[a], v[b], v[c]])
                    while b+1 < c and v[b+1] == v[b]: b += 1
                    while c-1 > b and v[c-1] == v[c]: c -= 1
                    b += 1
                    c -= 1
                elif v[a]+v[b]+v[c] < s:
                    b += 1
                else:
                    c -= 1
            while a+1 < len(v) and v[a+1] == v[a]: a += 1
            a += 1
        print(r)

three_sum([1,4,16,6,10,8,2], 22)
all_three_sum([1,4,16,6,10,8,2], 22)
