import time

count = 0

def fib2(n: int) -> int:
    global count
    count += 1
    if n < 2: # Abbruchbedingung
        return n
    return fib2(n-1) + fib2(n-2)


if __name__ == "__main__":

    # Liste der Fibonaci Zahlen von 0 .. 29
    for i in range(30):
        count = 0 # Anzahl der Aufrufe der fib Funktion.
        start_time=time.time()
        x = fib2(i)
        ende_time=time.time()
        print("fib2({:.0f}) = {:.0f}: Aufrufe: {:.0f}:  Laufzeit: {:5.3f}s".format(i, x, count, ende_time-start_time) )
    