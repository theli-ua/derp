#/bin/env python
def maxFlow(cap,s,t):
    def findPath(u,f):
        if u == t:
            return f
        vis[u] = True
        for v in xrange(len(vis)):
            if not vis[v] and cap[u][v] > 0:
                if f == -1: f = cap[u][v]
                df = findPath(v, min(f,cap[u][v]))
                if df > 0:
                    cap[u][v] -= df
                    cap[v][u] += df
                    return df
        return 0
    vis = [False] * len(cap)
    flow = 0

    df = findPath(s, -1)
    while df != 0:
        flow += df
        df = findPath(s, -1)
    return flow




if __name__ == '__main__':
    print maxFlow( [ [0,3,2], [0,0,2], [0,0,0] ], 0, 2)
