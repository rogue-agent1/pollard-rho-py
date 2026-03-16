#!/usr/bin/env python3
"""Pollard's rho — integer factorization."""
import math, random

def is_prime(n):
    if n < 2: return False
    for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n == a: return True
        if n % a == 0: return False
        d, r = n-1, 0
        while d%2==0: d//=2; r+=1
        x = pow(a, d, n)
        if x==1 or x==n-1: continue
        for _ in range(r-1):
            x = pow(x,2,n)
            if x==n-1: break
        else: return False
    return True

def pollard_rho(n):
    if n % 2 == 0: return 2
    x = random.randint(2,n-1); y = x; c = random.randint(1,n-1); d = 1
    while d == 1:
        x = (x*x+c)%n; y = (y*y+c)%n; y = (y*y+c)%n
        d = math.gcd(abs(x-y), n)
    return d if d != n else None

def factorize(n):
    if n <= 1: return []
    if is_prime(n): return [n]
    d = None
    while d is None or d == n: d = pollard_rho(n)
    return sorted(factorize(d) + factorize(n//d))

def main():
    for n in [12, 1000000007, 123456789]:
        print(f"{n} = {factorize(n)}")

if __name__ == "__main__": main()
