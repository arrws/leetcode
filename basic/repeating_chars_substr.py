import collections

def longest_nonrep(s):
    # len longest substr with nonrepeating characters
    if s == "": return 0
    d = {}
    l = 0
    last = 0
    # use last i window to be the substring
    for i in range(len(s)):
        if d.get(s[i], -1) != -1: # if repeating character
            last = max(last, d[s[i]]+1) # shift last
        d[s[i]] = i # where last the letter s[i] was seen
        l = max(l, i-last+1)
    return l

def mod_longest_nonrep(s, k):
    # replace k letters, find len longest substr of nonrep ch
    if s == "": return 0
    d = {}
    l = 0
    last = [0]
    # same but with a queue
    for i in range(len(s)):
        if d.get(s[i], -1) != -1:
            last.append(max(last[-1], d[s[i]]+1))
            if len(last) > k+1:
                last.pop(0)
        d[s[i]] = i
        l = max(l, i-last[0] +1)
    return l

def mod_longest_rep(s, k):
    # replace k letters, find len longest substr of rep ch
    if s == "": return 0
    d = collections.defaultdict(int)
    l = 0
    j = 0
    ch = 0
    # maintain in between j and i the substr
    for i in range(len(s)):
        d[s[i]] += 1 # keep track of letter freq in between j and i
        ch = max(ch, d[s[i]])
        # check if modified letters > k
        if i - j + 1 - ch > k: # if substr not valid increment j to revalidate
            d[s[j]] -= 1
            j += 1
        l = max(l, i - j + 1)
    return l

print(longest_nonrep("abcabcbb"))
print(mod_longest_rep("aababba", 2))
print(mod_longest_nonrep("aababba", 2))

