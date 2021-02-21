# swap 2 values inplace with XOR
a = a^b
b = a^b
a = a^b

# check the value of the ith bit
def getBit(num, i):
    return ((num & (1 << i)) != 0);

# set value of the ith bit
def set_bit_to_one(num, i): return num | (1 << i)
def set_bit_to_zero(num, i): return num & (~(1 << i))
def set_bit(num, i, value):
    mask = ~(1 << i)
    return (num & mask) | (value << i)

# clear rightmost bit
def clearRightmost(num): return num & (num-1)

# pop! count the number of 1 bits
def pop_count(x):
    n = 0;
    while (x):
        n += 1
        x = x & (x-1) # clear rightmost
    return n

# count the number of 1 bits bit by bit
def count_ones(x):
    n = 0
    while x:
        n += x & 1
        x >>= 1
    return n

# Hamming distance: number of different bits beetween 2 integers
def hamming_dist(x, y): return pop_count(x^y)

# sum a and b without using plus
def get_sum(a, b):
    # print(bin(a), bin(b), bin(a+b))
    while b:
        tmp = a ^ b
        b = (a & b) << 1
        a = tmp
        # print(bin(a), bin(b))
    return a

def count_all_ones(x):
        # 0000 0

        # 0001 1 - 1th

        # 0010 1 - 2th
        # 0011 2

        # 0100 1 - 4th
        # 0101 2
        # 0110 2
        # 0111 3

        # 1000 1 - 8th
        # 1001 2
        # 1010 2
        # 1011 3
        # 1100 2
        # 1101 3
        # 1110 3
        # 1111 4

        a = [0, 1]
        k = 2
        j = 0
        for i in range(2, x+1):
            if i == k:
                j = 0
                k *= 2
            a.append(a[j]+1)
            j += 1
        return a

def rev_bit_order(n):
    # print(n, bin(n))
    x = 0
    for _ in range(31): # for 32 bits
        if n & 1 == 1: x |= 1
        x <<= 1
        n = n >> 1
    if n & 1 == 1: x |= 1
    return x

print(get_sum(5,3))
print(count_ones(20))
print(count_all_ones(20))
print(rev_bit_order(20))

