from sys import stdin
import re

T = int(stdin.readline())

results = ['X won', 'O won', 'Draw', 'Game has not completed']

X_winning = [
        'XXXX............',
        '....XXXX........',
        '........XXXX....',
        '............XXXX',
        'X...' * 4,
        '.X..' * 4,
        '..X.' * 4,
        '...X' * 4,
        'X....X....X....X',
        '...X..X..X..X...'
        ]

O_winning = [x.replace('X','O') for x in X_winning]

re_X = re.compile('(' + '|'.join(X_winning) + ')')
re_O = re.compile('(' + '|'.join(O_winning) + ')')

for i in xrange(1,T+1):
    X = ''.join(stdin.readline().strip() for _ in xrange(4))
    stdin.readline()
    has_empty = '.' in X
    O = X.replace('T','O').replace('X','.')
    X = X.replace('T','X').replace('O','.')

    if re_X.match(X):
        result = 0
    elif re_O.match(O):
        result = 1
    elif has_empty:
        result = 3
    else:
        result = 2
    print 'Case #{0}: {1}'.format(i, results[result])

