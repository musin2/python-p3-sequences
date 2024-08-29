#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if length > 0:
         fib.append(0)
    if length > 1:
        fib.append(1)
    if length >=2:
     for n in range(2,length):
        # i = fib.index(n)
        i = fib[n-1] + fib[n-2]
        fib.append(i)

    print(fib)

print_fibonacci(9)