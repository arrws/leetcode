import random
import math


def pow_log_time(n, p):
    s = 1
    while p:
        # print(n, p, s)
        if p%2 == 1:
            s *= n
        p = p>>1
        n = n*n
    return s



def erathostene_siege(n):
    u = [True for _ in range(n+1)]
    primes = [2]
    for x in range(3, n+1, 2):
        if u[x]:
            primes.append(x)
            for y in range(x*x, n+1, 2*x):
                u[y] = False
    return primes


def majority(a):
    i = 0
    for x in a:
        if i == 0:
            m = x
            i = 1
        elif m == x:
            i += 1
        else:
            i -= 1
    return m

# print(majority([1,1,2,1,2,3,5,8,5,5,6,2,1,5,5,5,3,2,2,2,1,2,8,8,2,8,8,8,3,2,2]))


def fib(n):
    if n < 4:
        return n
    x, y = 2, 3
    for _ in range(4, n+1):
        x, y = y, x+y
    return y

def fast_fib(n):
    # log n time
    m = math.sqrt(5)
    x = math.pow((1+m)/2, n+1) - math.pow((1-m)/2, n+1)
    return int(x/m)




# 0| 0 1 2 3 4
# ------------
# 0| 0 1 2 3 4
# 1| 5 6 0 1 2
# 2| 3 4 5 6 0
# 3| 1 2 3 4 5
# 4| 6 - - - -

def rand7_from_rand5():
    def rand5(): pass

    x = 5*rand5() + rand5()
    while x > 20:
            x = 5*rand5() + rand5()
    return s%7;



# pick random number weighted by value

def bin_search(x, arr):
    l, r = 0, len(arr)-1
    while l < r:
        m = l + (r - l) // 2
        if x > arr[m]:
            l = m + 1
        else:
            r = m
    return l

class RandomPicker():

    def __init__(self, weights):
        self.sum = sum(weights)
        for i in range(1, len(weights)):
            weights[i] += weights[i - 1]
        self.arr = weights
        # print(self.sum, self.arr)

    def pickIndex(self):
        x = random.randint(1, self.sum)
        return bin_search(x, self.arr)

# p = RandomPicker([1,3,1,2,6,  2,1 ,3])
# print(p.pickIndex())

