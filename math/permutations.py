
def gen_perm_recursive(word):
    def fun(sol, word):
        if word == []:
            print("".join(sol))
        for i, x in enumerate(word):
            fun(sol+[x], word[:i]+word[i+1:])

    word = [x for x in word]
    fun(sort(word), [])

def gen_perm_iterative(word):
    word = [x for x in sort(word)]
    q = [[[], word]]
    while len(q) > 0:
        sol, word = q.pop(-1)
        if word == []:
            print("".join(sol))
        for i, x in enumerate(word):
            q.append([sol+[x], word[:i]+word[i+1:]])

def gen_rand_perm(v):
    import random
    for i in range(len(v)-1):
        x = random.randint(1, len(v)-i-1)
        x += i
        v[i], v[x] = v[x], v[i]
    print(v)

gen_perm_recursive("abcdef")
gen_perm_iterative("abcdef")
gen_rand_perm([1,2,3,4,5,6,7,8,9])
gen_rand_perm([1,2,3,4,5,6,7,8,9])
gen_rand_perm([1,2,3,4,5,6,7,8,9])


