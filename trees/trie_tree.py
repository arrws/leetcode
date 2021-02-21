class Node:
    def __init__(self):
        self.a = [None]*26 # only 'a-z'
        # self.a = collections.defaultdict(TrieNode)
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def _convert(self, x):
        return ord(x)-ord('a')

    def insert(self, word):
        r = self.root
        for k in range(len(word)):
            idx = self._convert(word[k])
            # if current character is not present
            if not r.a[idx]:
                r.a[idx] = Node()
            r = r.a[idx]
        r.end = True

    # def insert(self, word):
        # r = self.root
        # for c in word:
        #     r = r.a[c]
        # r.end = True

    def search(self, word):
        r = self.root
        for k in range(len(word)):
            idx = self._convert(word[k])
            # if current character is not present
            if not r.a[idx]:
                return False
            # else go on searching
            r = r.a[idx]
        return r != None and r.end

    # def search(self, word):
    #     r = self.root
    #     for c in word:
    #         r = r.a.get(c)
    #         if not r:
    #             return False
    #     return r.end

    # def search_star(word):
    #     # search with wildcard
    #     def find(r, word):
    #         if len(word) == 0:
    #             return r.end
    #         if word[0] == '.':
    #             return any(find(y, word[1:]) for y in r.a.values())
    #         y = r.a.get(word[0])
    #         if not y:
    #             return False
    #         return find(y, word[1:])
    #     return find(self.root, word)


t = Trie()
for word in ["the","a","there","anaswe","any","by","their"]:
    t.insert(word)

print(t.search("the"))
print(t.search("these"))
print(t.search("their"))
print(t.search("thaw"))

