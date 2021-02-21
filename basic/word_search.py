import collections

class TrieNode:
    def __init__(self):
        self.w = False
        self.l = collections.defaultdict(TrieNode)

class WordSearch:
    def findWords(self, board, words):
        N = len(board)
        M = len(board[0])
        self.r = []

        t = TrieNode()
        def insert(t, word):
            for c in word:
                t = t.l[c]
            t.w = True

        for word in words:
            insert(t, word)

        def moves(i, j):
            return zip([i, i, i-1, i+1], [j-1, j+1, j, j])

        def dfs(t, word, k, i, j):
            if t.w == True:
                self.r.append(word)
                t.w = False

            if 0 <= i < N and 0 <= j < M:
                u = board[i][j]
                t = t.l.get(u)
                if not t: return

                board[i][j] = -1
                for x, y in moves(i,j):
                    dfs(t, word + u, k + 1, x, y)
                board[i][j] = u

        for i in range(N):
            for j in range(M):
                dfs(t, '', 0, i, j)
        return self.r

w = WordSearch()
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
print(w.findWords(board, ["oath","pea","eat","rain"]))

