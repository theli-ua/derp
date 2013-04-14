from sys import stdin

T = int(stdin.readline())

for i in xrange(1, T+1):
    possible = True
    N,M = map(int, stdin.readline().split())
    lawn = [map(int,stdin.readline().split()) for _ in xrange(N)]
    for x in xrange(M):
        for y in xrange(N):
            if lawn[y][x] != max(lawn[y]):
                if lawn[y][x] != max(z[x] for z in lawn):
                    possible = False
                    break
        if not possible: break

    if possible:
        print 'Case #{0}: YES'.format(i)
    else:
        print 'Case #{0}: NO'.format(i)
