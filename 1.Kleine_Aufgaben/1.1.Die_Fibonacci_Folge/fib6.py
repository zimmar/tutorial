import time
from typing import Generator

count = 0

def fib6(n: int) -> Generator[int, None, None]:
    global count
    count += 1
    yield 0 # Spezialfall
    if n > 0: yield 1 # Spezialfall
        
    last: int = 0 # Am Anfang auf fib(0) setzen
    next: int = 1 # Am Anfang auf fib(1) setzeb
    for _ in range(1, n):
        last, next = next, last + next
        yield next
    

if __name__ == '__main__':
    
    # Liste der Fibonaci Zahlen von 0 .. 29
    for i in fib6(50):
        print(i)
    