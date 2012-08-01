def insertionsort(l):
    for i in xrange(1,len(l)):
        x = l[i]
        i -= 1
        while i >= 0 and l[i] > x:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = x

if __name__ == '__main__':
    from random import randint
    testdata = [randint(-100,100) for _ in range(40)]
    sorteddata = sorted(list(testdata))

    print testdata
    print sorteddata
    insertionsort(testdata)
    print testdata
