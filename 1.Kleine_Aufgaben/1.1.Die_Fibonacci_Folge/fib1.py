def fib1(n: int) -> int:
    return fib1(n-1) + fib1(n-2)


if __name__ == "__main__":

    # Liste der Fibonaci Zahlen von 0 .. 29
    for i in range(30):
        print(fib1(i))