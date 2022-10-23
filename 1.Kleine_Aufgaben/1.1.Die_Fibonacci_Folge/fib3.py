from typing import Dict 
import time

count = 0

memo: Dict[int, int] = {0: 0, 1: 1} # Abbruchbedingung
def fib3(n: int) -> int:
    global count
    count += 1
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n -2) # Memoisation
    return memo[n]

if __name__ == '__main__':
    
    # Liste der Fibonaci Zahlen von 0 .. 29
    for i in range(30):
        count = 0 # Anzahl der Aufrufe der fib Funktion.
        start_time=time.time()
        x = fib3(i)
        ende_time=time.time()
        print("fib3({:.0f}) = {:.0f}: Aufrufe: {:.0f}:  Laufzeit: {:5.3f}s".format(i, x, count, ende_time-start_time) )