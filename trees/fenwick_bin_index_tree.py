# returns sum of arr[0..i], assumes partial sums
def get_sum(tree,i):
    r = 0
    i = i+1
    while i>0:
        r += tree[i]    # add current element to sum
        i -= i & (-i)   # move index to parent node
    return r

# updates node at given index
def update(tree, i, v):
    i += 1
    while i<len(tree):
        tree[i] += v    # add value to current node
        i += i & (-i)   # update index to parent
    return tree

# return a Binary Indexed Tree
def build(arr):
    n = len(arr)
    tree = [0]*(n+1)    # initialization
    for i in range(n):
        update(tree, i, arr[i])
    # for x in tree: print (x, end=", ")
    return tree

tree = build([2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9])
print("")
print("sum arr[0..5]: " + str(get_sum(tree,5)))
tree = update(tree, 3, 6)
print("after update: " + str(get_sum(tree,5)))
