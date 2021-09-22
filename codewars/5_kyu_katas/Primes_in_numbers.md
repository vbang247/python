## Primes in numbers
**Instructions**

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
```Python
 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.
```
```Python
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
```
### Given Code
```python
def prime_factors(n):
    ...
```
---
### Solution
```python
def prime_factors(n):
    factors = []
    i = 2
    while(n > 1):
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i = i+1
    
    return_str = ''
    new_list = list(set(factors))
    for j in sorted(new_list):
        if(factors.count(j) > 1):
            return_str = return_str + "({}**{})".format(j, factors.count(j))
        else:
            return_str = return_str + "({})".format(j)
    return return_str
```
---
[See on CodeWars.com](https://www.codewars.com/kata/54d512e62a5e54c96200019e)
