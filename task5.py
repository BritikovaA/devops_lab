#!/usr/bin/env python
# coding: utf-8

n = int(input())
matr = []
diag = undiag = 0
for i in range(n):
    matr.append([int(j) for j in input().split()])
for k in range(n):
    diag += matr[k][k]
    undiag += matr[k][- 1 - k]
num = abs(diag - undiag)
print(num)
