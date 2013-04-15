from sys import stdin
from collections import Counter

T = int(stdin.readline())

global bads
bads = []

def check(keys, visited, chests, path):
    if len(path) == len(chests):
        return path
    if frozenset(path) in bads: 
        return None
    for k in xrange(len(chests)):
        if not visited[k]:
            if chests[k][0] in keys:
                i = keys.index(chests[k][0])
                visited[k] = True
                res = check(keys[:i] + keys[i+1:] + chests[k][1:], 
                        visited, chests, path + [k])
                if res is not None:
                    return res
                visited[k] = False
    bads.append(frozenset(path))
    return None

for i in xrange(1, T+1):
    bads = []
    K,N = map(int, stdin.readline().split())
    keys = map(int, stdin.readline().split())
    chests = [map(int, stdin.readline().split()) for _ in xrange(N)]
    visited = [False] * N

    keys_across_universe = Counter(keys + sum([chest[1:] for chest in chests],[]))
    required = Counter(chest[0] for chest in chests)
    if all((required[r] <= keys_across_universe[r] for r in required)):
        res = check(keys, visited, chests, [])
    else:
        res = None

    if res is None:
        print 'Case #{0}: IMPOSSIBLE'.format(i)
    else:
        print 'Case #{0}: {1}'.format(i, ' '.join(map(lambda x: str(x+1),res)))
