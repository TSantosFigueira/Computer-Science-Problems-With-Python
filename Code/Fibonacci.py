from typing import Generator

def fibonnaci(n):
    if n == 0: return 0
    prev = 0
    next = 1
    for _ in range(n):
        prev, next = next, prev + next
    
    return next

def fibonnaci_generator(n):
    yield 0
    if n > 0:
        yield 1
    prev = 0
    next = 1
    for _ in range(1, n+1):
        prev, next = next, prev + next
        yield next

n = 10
print(fibonnaci(n))
for i in fibonnaci_generator(n):
    print(i, end=' ')