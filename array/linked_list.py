class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    prev = None
    x = head
    while x != None:
        link = x.next
        x.next = prev
        prev = x
        x = link
    return prev


def hasCycle(head):
    if not head or not head.next:
        return False
    p = head
    fast_p = head
    while fast_p and fast_p.next:
        p = p.next
        fast_p = fast_p.next.next
        if p == fast_p:
            return True
    return False


def mergeTwoLists(l1, l2):
    head = l = Node(0)
    while l1 and l2:
        if l1.val > l2.val:
            l.next = l2
            l2 = l2.next
        else:
            l.next = l1
            l1 = l1.next
        l = l.next
    if l1:
        l.next = l1
    if l2:
        l.next = l2
    return head.next


def mergeKLists(lists):
    if lists == []: return []
    if len(lists) == 1: return lists[0]
    while len(lists) > 1:
        l = []
        for  i in range(0, len(lists)-1, 2):
            l.append(mergeTwoLists(lists[i], lists[i+1]))
        if len(lists) % 2 == 1:
            l.append(lists[-1])
        lists = l
    return lists[0]

def removeNth(head, n):
    # assume n < len(list)
    p = head
    for _ in range(n+1):
        p = p.next
    if p.next.next:
        p.next = p.next.next
    else:
        p.next = None
    return head

def removeNthFromEnd(head, n):
    l = Node(0)
    l.next = head
    p = l
    fast_p = l
    for _ in range(n):
        fast_p = fast_p.next
    while fast_p.next:
        p = p.next
        fast_p = fast_p.next
    p.next = p.next.next
    return l.next


def nextLargerNodes(head):
# return array with the next larger element
    # ex: input [1,7,5,1,9,2,5,1], output: [7,9,9,9,0,5,0,0]
    while head:
        while s and s[-1][0] < head.val:
            _, i = s.pop(-1)
            a[i] = head.val
        a.append(0)
        s.append([head.val, k])
        k += 1
        head = head.next
    return a

def isPalindrome(self, head: Node) -> bool:
    # O(N) time O(1) space
    p = None
    x = head
    y = head

    # reverse first half
    while y != None and y.next != None:
        y = y.next.next
        u = x.next
        x.next = p
        p = x
        x = u

    # middle elem edgecase
    if y:
        x = x.next

    # compare halfs
    while p != None and x != None:
        if p.val != x.val:
            return False
        p = p.next
        x = x.next
    return True


def find_intersect_point(headA, headB):
    if headA == None or headB == None:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a



