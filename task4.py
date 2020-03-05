#!/usr/bin/env python

def func(num):
    if num >= 0 and num <= 9:
        return num
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
        return -1
    else:
        return k

if __name__ == "__main__":
  n = int(input("Input number:"))
  print(func(n))
