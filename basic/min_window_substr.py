import collections
"""
min substring from s wich contains all characters from t
"""

def min_window(s, t):
    min_window = s + t
    target_d = collections.Counter(t)
    target_num_letters = len(target_d.keys())
    d = {x: 0 for x in target_d.keys()}

    # reduce string to only letters of interest
    # arr = [[letter, s_index], ...]
    arr = []
    for i in range(len(s)):
        if target_d.get(s[i], -1) != -1:
            arr.append([s[i], i])

    k = 0       # current num letters
    i, j = 0, 0 # current window from index at i to j
    while j < len(arr):
        letter, idx = arr[j]

        # expand window to right
        d[letter] += 1
        if d[letter] == target_d[letter]:
            k += 1

        # if having all letters in window
        # maybe shrink window from left
        while k == target_num_letters:
            # first letter, index from window
            prev_letter, prev_idx = arr[i]

            # if window without first letter valid
            window = s[prev_idx:idx+1]
            if len(min_window) > len(window):
                min_window = window

            # remove first letter from window
            d[prev_letter] -= 1
            if d[prev_letter] < target_d[prev_letter]:
                k -= 1

            i += 1
        j += 1

    if len(min_window) < len(t) or len(min_window) > len(s):
        return ""
    return min_window

print(min_window("adobecodebancuoa", "abc"))

