import time
from functools import lru_cache

count = 0

@lru_cache(maxsize=None)
def fib4(n: int) -> int: # Die selbe Diefinition wie fib2
    global count
    count += 1
    if n < 2: # Abbruchbedingung
        return n
    return fib4(n - 2) + fib4(n - 1)

if __name__ == '__main__':
    
    # Liste der Fibonaci Zahlen von 0 .. 29
    for i in range(30):
        count = 0 # Anzahl der Aufrufe der fib Funktion.
        start_time=time.time()
        x = fib4(i)
        ende_time=time.time()
        print("fib4({:.0f}) = {:.0f}: Aufrufe: {:.0f}:  Laufzeit: {:5.3f}s".format(i, x, count, ende_time-start_time) )