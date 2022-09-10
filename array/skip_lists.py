# Skiplist data structure takes O(log(n)) time to add, erase or search.
# ^ levels added up
# 30 -------------------------------------> None
# 30 -------> 50 -------------------------> None
# 30 -------> 50 -------> 70 -> 80 -------> None
# 30 -> 40 -> 50 -> 60 -> 70 -> 80 -> 90 -> None

import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

    def __repr__(self):
         return f"({self.val}, {self.down}, {self.next})"

class Skiplist:

    def __init__(self):
        self.root = Node(-1);

    def search(self, num: int) -> bool:
        levels = self._get_level_rightmost(self.root, num)
        x = levels[0].next
        return x and x.val == num

    def _insert(self, x: Node, num: int) -> Node:
        # insert new node after x
        y = Node(num)
        y.next = x.next
        x.next = y
        return y

    def _coin_flip(self) -> bool:
        return bool(random.getrandbits(1))

    def add(self, num: int) -> None:
        levels = self._get_level_rightmost(self.root, num)
        # add item on last level (0) then add on coinflip
        prev_y = None
        for i, x in enumerate(levels):
            if self._coin_flip() or i == 0:
                y = self._insert(x, num)
                y.down = prev_y
                prev_y = y
            else:
                return
        # maybe add new level if all coinflips passed
        if self._coin_flip():
            new_root = Node(-1)
            new_root.down = self.root
            self.root = new_root
            y = self._insert(self.root, num)
            y.down = prev_y

    def _get_level_rightmost(self, x: Node, num: int):
        levels = []
        while x:
            while x.next and x.next.val < num:
                x = x.next
            levels.append(x)
            x = x.down
        return levels[::-1]

    def erase(self, num: int) -> bool:
        levels = self._get_level_rightmost(self.root, num)
        ok = False
        for x in levels:
            if x.next and x.next.val == num:
                x.next = x.next.next
                ok = True
            else:
                break
        return ok

