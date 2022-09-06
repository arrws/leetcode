
import itertools

def quick_sort(v, l, r):
    # avg O(nlogn), worst O(n^2)
    if l < r:
        pivot = v[r]
        j = l
        for i in range(l, r):
            if v[i] < pivot:
                v[i], v[j] = v[j], v[i]
                j += 1
        v[r], v[j] = v[j], v[r]
        quick_sort(v, l, j-1)
        quick_sort(v, j+1, r)

for v in itertools.permutations([1,7,8,8,9,5]):
    v = list(v)
    quick_sort(v, 0, len(v)-1)
    print(v)


# find kth element / sort first k elems
def quick_select(k, v):
    # avg O(n), wors O(n^2)
    if k <= len(v):
        pivot = v[-1]
        j = 0
        for i in range(len(v)):
            if v[i] < pivot:
                v[i], v[j] = v[j], v[i]
                j += 1
        v[-1], v[j] = v[j], v[-1]

        if j == k-1:
            return v[j]
        elif j < k-1:
            return quick_select(k-j-1, v[j+1:])
        else:
            return quick_select(k, v[:j])
    return -1

print(quick_select(3, [10,7,8,9,1,2,5]))


def merge_sort(v):

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

    if len(v) < 2:
        return v
    mid = len(v)//2
    left = merge_sort(v[:mid])
    right = merge_sort(v[mid:])
    return merge(left, right)

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


v = [10,7,8,9,1,2,5]
v = merge_sort(v)
# insertion_sort(v)
# selection_sort(v)
# bubble_sort(v)
print(v)


def radix_sort_digit(arr):

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

    maxn = max(arr) # max num for num digits
    e = 1
    while maxn//e > 0:
        arr = counting_sort(arr, e) # do sort on each digit
        e *= 10
    return arr

def radix_sort_bit(arr):
    for bit in range(32):
        j = 0
        for i in range(len(arr)):
            if arr[i] & (1 << bit) == 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        print(arr)
    return arr


arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort_bit(arr))
print(radix_sort_digit(arr))


