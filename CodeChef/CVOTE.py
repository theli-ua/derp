#!/bin/env python
from sys import stdin
VOTES_COUNTRIES = {}
VOTES_CHEFS = {}
CHEF_COUNTRIES = {}
N,M = (int(x) for x in stdin.readline().split())

for _ in xrange(N):
    chef,country = stdin.readline().split()
    CHEF_COUNTRIES[chef] = country
    VOTES_COUNTRIES[country] = 0
    VOTES_CHEFS[chef] = 0

for _ in xrange(M):
    m = stdin.readline().strip()
    VOTES_CHEFS[m] += 1
    VOTES_COUNTRIES[CHEF_COUNTRIES[m]] += 1

print sorted([(-VOTES_COUNTRIES[c],c) for c in VOTES_COUNTRIES.keys()])[0][1]
print sorted([(-VOTES_CHEFS[c],c) for c in VOTES_CHEFS.keys()])[0][1]
