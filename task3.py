#!/usr/bin/env python
# coding: utf-8

string = input().split(' ')
newstr = []
for i in range(len(string)):
    newstr.append(string[i][len(string[i])::-1])
print(*newstr, sep = " ")
