
def quick_sort(v, l, h):
    # best nlogn, worst n^2
    if l < h:
        p = v[h]
        i = l
        for j in range(l+1, h-1):
            if v[j]< p:
                v[i], v[j] = v[j], v[i]
                i += 1
        v[i], v[h] = v[h], v[i]
        quick_sort(v, l, i-1)
        quick_sort(v, i+1, h)

v = [10,7,8,9,1,2,5]
quick_sort(v, 0, len(v)-1)
print(v)


def quick_select(k, v):
    # best nlogn, worst n^2
    if k <= len(v):
        p = -1
        i = 0
        for j in range(len(v)):
            if v[j]< v[p]:
                v[i], v[j] = v[j], v[i]
                i += 1
        v[i], v[p] = v[p], v[i]

        if i == k-1:
            return v[i]
        elif i < k-1:
            return quick_select(k-i-1, v[i+1:])
        else:
            return quick_select(k, v[:i])
    return -1


v = [10,7,8,9,1,2,5]
min_k = quick_select(3, v)
print(min_k)



def merge(left, right):
    i = j = 0
    v = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            v.append(left[i])
            i += 1
        else:
            v.append(right[j])
            j += 1
    while i < len(left):
        v.append(left[i])
        i += 1
    while j < len(right):
        v.append(right[j])
        j += 1
    return v


def merge_sort(v):
    if len(v) < 2:
        return v
    mid = len(v)//2
    left = merge_sort(v[:mid])
    right = merge_sort(v[mid:])
    return merge(left, right)

v = [10,7,8,9,1,2,5]
v = merge_sort(v)
print(v)


def insertion_sort(v):
    for i in range(len(v)):
        for j in range(i,0,-1):
            if v[j-1] > v[j]:
                v[j], v[j-1] = v[j-1], v[j]

def selection_sort(v):
    for i in range(len(v)):
        k = i
        for j in range(i+1, len(v)):
            if v[k] > v[j]:
                k = j
        if k != i:
            v[i], v[k] = v[k], v[i]

def bubble_sort(v):
    for i in range(len(v)):
        ok = 1
        for j in range(1, len(v)):
            if v[j] < v[j-1]:
                v[j], v[j-1] = v[j-1], v[j]
                ok = 0
        if ok == 1: break


# v = [10,7,8,9,1,2,5]
# insertion_sort(v)
# selection_sort(v)
# bubble_sort(v)
# print(v)


def counting_sort(arr, e):
    n = len(arr)
    a = [0 for _ in range(n)]   # sorted array
    c = [0 for _ in range(10)]  # counts array

    # count of occurrences
    for i in range(0, n):
        c[(arr[i]//e) % 10] += 1

    # compute actual position of this digit in output array
    for i in range(1, 10):
        c[i] += c[i-1]

    # build the sorted array
    for i in range(n-1, -1, -1):
        idx = (arr[i]//e) % 10 # index of current number
        a[c[idx]-1] = arr[i]
        c[idx] -= 1

    return a

def radix_sort(arr):
    maxn = max(arr) # max num for num digits
    e = 1
    while maxn//e > 0:
        arr = counting_sort(arr, e) # do sort on each digit
        e *= 10
    return arr

arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))


