def next_greater_elem(a):
    r = {}
    # put first elem on a stack
    s = [a[0]]
    for y in a[1:]:
        if len(s) > 0:
            # while elem in stack < current elem
            x = s.pop(-1)
            while x < y:
                # assign current elem as next greater
                r[x] = y
                if len(s) == 0:
                    break
                x = s.pop(-1)
            # put current elem on the stack
            if x > y:
                s.append(x)
        s.append(y)
    # elem left on stack have no next greater
    while len(s) > 0:
        r[s.pop(0)] = -1
    return r

a = [11, 13, 21, 3]
print(next_greater_elem(a))
a.reverse()
print(next_greater_elem(a))
