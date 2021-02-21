# given an positive int array, what is the minimum largest sum among n subarrays.

def split_arr_min_sums(v, n):
    max_elem = max(v)
    max_sum = sum(v)

    if len(v) == n:
        return max_elem

    while max_elem <= max_sum:
        mid = (max_elem+max_sum) // 2
        # print(mid)
        k = 1
        s = 0
        for x in v:
            if s + x <= mid:
                s += x
            else:
                k += 1
                s = x
                if k > n:
                    break
        if k <= n:
            max_sum = mid-1
        else:
            max_elem = mid+1
    return max_elem

print(split_arr_min_sums([7,2,5,10,8], 2))
