def mergesort(l):
    def _merge(l,p,q,r):
        L1 = l[p:q + 1]
        L2 = l[q + 1:r + 1]
        len1 = len(L1)
        len2 = len(L2)
        i1 = 0
        i2 = 0
        i = p
        for i in xrange(p,r+1):
            if i2 >= len2:
                l[i] = L1[i1]
                i1 += 1
            elif i1 >= len1 or L2[i2] < L1[i1]:
                l[i] = L2[i2]
                i2 += 1
            else:
                l[i] = L1[i1]
                i1 += 1
    def _merge_sort(l,p,r):
        if p < r:
            q = p + (r - p)/2
            _merge_sort(l,p,q)
            _merge_sort(l,q+1,r)
            _merge(l,p,q,r)
    _merge_sort(l,0,len(l)-1)

if __name__ == '__main__':
    from random import randint
    testdata = [randint(-100,100) for _ in range(40)]
    sorteddata = sorted(list(testdata))

    print testdata
    print
    print sorteddata
    mergesort(testdata)
    print testdata
    print testdata == sorteddata

