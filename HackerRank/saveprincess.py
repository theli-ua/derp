#!/bin/python
# Head ends here
MOVES = ['LEFT','RIGHT','UP','DOWN']
def displayPathtoPrincess(m,grid):
    m,p = (i for i,x in enumerate(grid) if x != '-')
    if grid[m] == 'p': m,p = p,m
    m,p = ((x/3, x%3) for x in [m,p])
    if m[0] > p[0]:
        v = 2
    else:
        v = 3
    if m[1] > p[1]:
        h = 0
    else:
        h = 1

    path = [v] * abs(m[0] - p[0])
    path.extend([h] * abs(m[1] - p[1]))
    return '\n'.join([MOVES[p] for p in path])
# Tail starts here


if __name__ == '__main__':
    print displayPathtoPrincess(3,'----m-p--')
