from itertools import product
from collections import deque

moves = [
            [ 1, 0, 0, 0 ],
            [ 0, 1, 0, 0 ],
            [ 0, 0, 1, 0 ],
            [ 0, 0, 0, 1 ],

            [-1, 0, 0, 0 ],
            [ 0,-1, 0, 0 ],
            [ 0, 0,-1, 0 ],
            [ 0, 0, 0,-1 ],
        ]

def solve(start, end, _bads):
    def move(word, m):
        res = [ord(x) - ord('a') for x in word]
        for i, mv in enumerate(m):
            res[i] += mv
            res[i] %= 26
        return ''.join([chr(x + ord('a')) for x in res])
    def all_moves(word):
        for i in moves:
            yield move(word, i)
    def visit(word):
        bads\
                [ord(word[0]) - ord('a')]\
                [ord(word[1]) - ord('a')]\
                [ord(word[2]) - ord('a')]\
                [ord(word[3]) - ord('a')] = True

    def isBad(word):
        return bads\
                [ord(word[0]) - ord('a')]\
                [ord(word[1]) - ord('a')]\
                [ord(word[2]) - ord('a')]\
                [ord(word[3]) - ord('a')]

    bads = [[[[False] * 26 for x in xrange(26)] for y in xrange(26)] for z in xrange(26)]
    for bad in _bads:
        bad = bad.split(' ')
        bad_words = [x for x in product(*bad)]
        for bad_word in bad_words:
            bads[ord(bad_word[0]) - ord('a')]\
                    [ord(bad_word[1]) - ord('a')]\
                    [ord(bad_word[2]) - ord('a')]\
                    [ord(bad_word[3]) - ord('a')] = True
    if isBad(end):
        return -1
    elif len(_bads) == 0:
        return \
            abs( ord(start[0]) - ord(end[0]) ) + \
            abs( ord(start[1]) - ord(end[1]) ) + \
            abs( ord(start[2]) - ord(end[2]) ) + \
            abs( ord(start[3]) - ord(end[3]) )

    else:
        stack = deque()
        stack.append( (start, 0) )

        while len(stack) > 0:
            #print stack
            current, cost = stack.popleft()
            visit(current)
            #print current, cost
            if current == end:
                return cost
            for word in all_moves(current):
                if not isBad(word):
                    if word == end:
                        return cost + 1
                    stack.append( (word, cost + 1) )
    return -1



start = "aaaa"
end = "zzzz"
bads = ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a"]
print solve(start, end, bads)

start = "aaaa"
end = "bbbb"
bads = []
print solve(start, end, bads)

start = "aaaa"
end = "mmnn"
bads = []
print solve(start, end, bads)

start = "aaaa"
end = "zzzz"
bads = ["bz a a a", "a bz a a", "a a bz a", "a a a bz"]
print solve(start, end, bads)


start = "aaaa"
end = "zzzz"
bads = ["cdefghijklmnopqrstuvwxyz a a a", 
 "a cdefghijklmnopqrstuvwxyz a a", 
 "a a cdefghijklmnopqrstuvwxyz a", 
 "a a a cdefghijklmnopqrstuvwxyz" ]
print solve(start, end, bads)

start = "aaaa"
end = "bbbb"
bads = ["b b b b" ]
print solve(start, end, bads)


start = "zzzz"
end = "aaaa"
bads = ["abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 "abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk",
 ]
print solve(start, end, bads)
