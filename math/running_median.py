import heapq

class RunningMedian:
    def __init__(self):
        # min heap is max heap with '-'
        self.right = [] # for min heap for elem > median
        self.left = [] # max heap for elem < median

    def addNum(self, num):
        heapq.heappush(self.right, -num)
        x = -heapq.heappop(self.right)
        heapq.heappush(self.left, x)

        if len(self.right) < len(self.left):
            x = heapq.heappop(self.left)
            heapq.heappush(self.right, -x)

    def findMedian(self): # returns float
        if len(self.right) > len(self.left):
            return float(-self.right[0])
        return float((-self.right[0] + self.left[0]) /2)

r = RunningMedian()
r.addNum(1)
r.addNum(2)
print(r.findMedian()) # 1.5
r.addNum(3)
print(r.findMedian()) # 2



def find_median(a, b):
    # given 2 sorted arrays find their combination median
    # O(log(n+m))

    m, n = len(a), len(b)
    if m > n:
        a, b, m, n = b, a, n, m

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and b[j-1] > a[i]:
            imin = i + 1
        elif i > 0 and a[i-1] > b[j]:
            imax = i - 1
        else:
            if i == 0:      mx = b[j-1]
            elif j == 0:    mx = a[i-1]
            else:           mx = max(a[i-1], b[j-1])

            if (m + n) % 2 == 1:
                return mx

            if i == m:      mn = b[j]
            elif j == n:    mn = a[i]
            else:           mn = min(a[i], b[j])

            return (mx + mn) / 2.0

print(find_median([1, 2], [3, 4]))

