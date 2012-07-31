def quicksort(A):
    def _partition(A,p,r):
        x = A[r]
        i = p - 1
        for j in xrange(p,r):
            if A[j] <= x:
                i += 1
                A[i],A[j] = A[j],A[i]
        A[i+1],A[r] = A[r],A[i+1]
        return i + 1
    def _quicksort(A,p,r):
        if p < r:
            q = _partition(A,p,r)
            _quicksort(A,p,q-1)
            _quicksort(A,q + 1, p)
    _quicksort(A,0,len(A) - 1)



if __name__ == '__main__':
    from random import randint
    testdata = [randint(-100,100) for _ in range(40)]
    sorteddata = sorted(list(testdata))

    print testdata
    print sorteddata
    quicksort(testdata)
    print testdata
