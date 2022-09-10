def longest_consec_seq_set(nums):
    # using sets
    # not O(N^2) but O(N) !!!
    nums = set(nums)
    max_len = 0

    for x in nums:
        if x - 1 not in nums:
            l = 1
            while x + 1 in nums:
                x += 1
                l += 1
            max_len = max(l, max_len)

    return max_len

# not taken in order
print(longest_consec_seq_set([1,4,16,6,10,8,2,10,4,20,1,3,2]))

