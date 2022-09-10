# given an positive int array, what is the minimum largest sum among n subarrays.

def split_arr_mn_sums(v, n):
    mn_sum = max(v) # smaller sum
    mx_sum = sum(v) # larger sum

    if len(v) == n:
        return mn_sum

    while mn_sum <= mx_sum:
        # tey to compute mid sum
        target_sum = (mn_sum + mx_sum) // 2

        k = 1 # num elems added
        s = 0 # current sum
        for x in v:
            # if can still add elem
            if s + x <= target_sum:
                s += x
            else:
                k += 1
                s = x
                if k > n:
                    break
        if k <= n:
            mx_sum = target_sum - 1
        else:
            mn_sum = target_sum + 1
    return mn_sum

print(split_arr_mn_sums([7,2,5,10,8], 2))
