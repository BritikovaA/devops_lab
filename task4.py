#!/usr/bin/env python
# coding: utf-8

num = int(input())
if num >= 0 and num <= 9:
    print(num)
digits = []
for i in range(9, 1, -1):
    while num % i == 0:
        digits.append(i)
        num = num // i
k = 0
while digits:
    k = k * 10 + digits[-1]
    digits.pop()
if k == 0:
    print(-1)
else:
    print(k)
