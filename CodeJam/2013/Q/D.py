from sys import stdin

T = int(stdin.readline())

def check(keys, visited, chests, path):
    print 'test path: ' + ' '.join(map(str,path))
    if len(path) == len(chests):
        return path
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
    return None

for i in xrange(1, T+1):
    K,N = map(int, stdin.readline().split())
    keys = map(int, stdin.readline().split())
    chests = [map(int, stdin.readline().split()) for _ in xrange(N)]
    visited = [False] * N

    res = check(keys, visited, chests, [])

    if res is None:
        print 'Case #{0}: IMPOSSIBLE'.format(i)
    else:
        print 'Case #{0}: {1}'.format(i, ' '.join(map(lambda x: str(x+1),res)))
