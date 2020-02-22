#!/usr/bin/python
# -*- coding: utf-8 -*-
"""caaronmachine.py: mle and bay proj."""

__author__ = 'Cameron Aaron'

import random

totallist = [
    1,
    2,
    3,
    4,
    5,
    6,
    6,
    6,
    6,
    6,
]

twenty = []
twohundred = []
twothousand = []


def bays(frq, prob, data):
    found = (prob**(frq)) * ((1 - prob)**((data - frq)))
    return found


for x in range(0, 20):
    twenty.insert(x, random.choice(totallist))

for x in range(0, 200):
    twohundred.insert(x, random.choice(totallist))

for x in range(0, 2000):
    twothousand.insert(x, random.choice(totallist))

onetwenty = twenty.count(1)
twotwenty = twenty.count(2)
threetwenty = twenty.count(3)
fourtwenty = twenty.count(4)
fivetwenty = twenty.count(5)
sixtwenty = twenty.count(6)

onetwohundred = twohundred.count(1)
twotwohundred = twohundred.count(2)
threetwohundred = twohundred.count(3)
fourtwohundred = twohundred.count(4)
fivetwohundred = twohundred.count(5)
sixtwohundred = twohundred.count(6)

onetwothousand = twothousand.count(1)
twotwothousand = twothousand.count(2)
threetwothousand = twothousand.count(3)
fourtwothousand = twothousand.count(4)
fivetwothousand = twothousand.count(5)
sixtwothousand = twothousand.count(6)

print(onetwenty)
print(twotwenty)
print(threetwenty)
print(fourtwenty)
print(fivetwenty)
print(sixtwenty)

print(onetwohundred)
print(twotwohundred)
print(threetwohundred)
print(fourtwohundred)
print(fivetwohundred)
print(sixtwohundred)
print(onetwothousand)
print(twotwothousand)
print(threetwothousand)
print(fourtwothousand)
print(fivetwothousand)
print(sixtwothousand)

print(onetwenty / 20)
print(twotwenty / 20)
print(threetwenty / 20)
print(fourtwenty / 20)
print(fivetwenty / 20)
print(sixtwenty / 20)

print(onetwohundred / 200)
print(twotwohundred / 200)
print(threetwohundred / 200)
print(fourtwohundred / 200)
print(fivetwohundred / 200)
print(sixtwohundred / 200)

print(onetwothousand / 2000)
print(twotwothousand / 2000)
print(threetwothousand / 2000)
print(fourtwothousand / 2000)
print(fivetwothousand / 2000)
print(sixtwothousand / 2000)

print(bays(onetwenty, 1 / 6, 20))
print(bays(twotwenty, 1 / 6, 20))
print(bays(threetwenty, 1 / 6, 20))
print(bays(fourtwenty, 1 / 6, 20))
print(bays(fivetwenty, 1 / 6, 20))
print(bays(sixtwenty, 1 / 6, 20))

print(bays(onetwohundred, 1 / 6, 200))
print(bays(twotwohundred, 1 / 6, 200))
print(bays(threetwohundred, 1 / 6, 200))
print(bays(fourtwohundred, 1 / 6, 200))
print(bays(fivetwohundred, 1 / 6, 200))
print(bays(sixtwohundred, 1 / 6, 200))

print(bays(onetwothousand, 1 / 6, 2000))
print(bays(twotwothousand, 1 / 6, 2000))
print(bays(threetwothousand, 1 / 6, 2000))
print(bays(fourtwothousand, 1 / 6, 2000))
print(bays(fivetwothousand, 1 / 6, 2000))
print(bays(sixtwothousand, 1 / 6, 2000))

print(bays(onetwenty, 0.1, 20))
print(bays(twotwenty, 0.1, 20))
print(bays(threetwenty, 0.1, 20))
print(bays(fourtwenty, 0.1, 20))
print(bays(fivetwenty, 0.1, 20))
print(bays(sixtwenty, 0.5, 20))

print(bays(onetwohundred, 0.1, 200))
print(bays(twotwohundred, 0.1, 200))
print(bays(threetwohundred, 0.1, 200))
print(bays(fourtwohundred, 0.1, 200))
print(bays(fivetwohundred, 0.1, 200))
print(bays(sixtwohundred, 0.5, 200))

print(bays(onetwothousand, 0.1, 2000))
print(bays(twotwothousand, 0.1, 2000))
print(bays(threetwothousand, 0.1, 2000))
print(bays(fourtwothousand, 0.1, 2000))
print(bays(fivetwothousand, 0.1, 2000))
print(bays(sixtwothousand, 0.5, 2000))

print(bays(onetwenty, 0.12, 20))
print(bays(twotwenty, 0.12, 20))
print(bays(threetwenty, 0.12, 20))
print(bays(fourtwenty, 0.12, 20))
print(bays(fivetwenty, 0.12, 20))
print(bays(sixtwenty, 0.4, 20))

print(bays(onetwohundred, 0.12, 200))
print(bays(twotwohundred, 0.12, 200))
print(bays(threetwohundred, 0.12, 200))
print(bays(fourtwohundred, 0.12, 200))
print(bays(fivetwohundred, 0.12, 200))
print(bays(sixtwohundred, 0.4, 200))

print(bays(onetwothousand, 0.12, 2000))
print(bays(twotwothousand, 0.12, 2000))
print(bays(threetwothousand, 0.12, 2000))
print(bays(fourtwothousand, 0.12, 2000))
print(bays(fivetwothousand, 0.12, 2000))
print(bays(sixtwothousand, 0.4, 2000))
