#!/usr/bin/env python
# coding: utf-8

word = input()
k = 0
for i in range(int(len(word) / 2)):
    if(word[i] != word[len(word) - 1 - i]):
        k = 1
if(k == 0):
    print("yes")
else:
    print("no")
