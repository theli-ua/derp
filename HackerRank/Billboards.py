#!/bin/env python
N,K = [int(x) for x in raw_input().split()]
boards = [int(raw_input()) for x in xrange(N)]

def profit(current_profit, current_len,i):
    #print current_profit, current_len, i
    if i >= N: return current_profit
    _current_profit = 0
    if current_len < K:
        _current_profit = profit(current_profit + boards[i],
                current_len + 1,  i+1)
    current_profit = max(_current_profit, profit(current_profit, 0, i+1))
    return current_profit

#print boards
print profit(0,0,0)
