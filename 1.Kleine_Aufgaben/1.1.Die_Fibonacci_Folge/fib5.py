import time

count = 0

def fib5(n: int) -> int: # Die selbe Diefinition wie fib2
    global count
    count += 1
    if n == 0: # Abbruchbedingung
        return n
    last: int = 0 # Am Anfang auf fib(0) setzen
    next: int = 1 # Am Anfang auf fib(1) setzeb
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == '__main__':
    
    # Liste der Fibonaci Zahlen von 0 .. 29
    for i in range(30):
        count = 0 # Anzahl der Aufrufe der fib Funktion.
        start_time=time.time()
        x = fib5(i)
        ende_time=time.time()
        print("fib5({:.0f}) = {:.0f}: Aufrufe: {:.0f}:  Laufzeit: {:5.3f}s".format(i, x, count, ende_time-start_time) )