## Zu Beginn eine einfache Aufgabe, die sich mit kurzen Funktionen lösen lassen.

1.1 Die Fibonacci Folge

Fibonacci Folge ist eine Folge von Zahlen, in der jede folgende Zahl die Summe 
der beiden Vorgänger ist. Ausnahme: 1 und 2 Zahl

    Zahl    0   1   2   3   4   5   6    7    8    9   10 
            0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55 - ...

***Bedingung:*** Zahl 0 ist immer 0 und Zahl 1 ist immer 1

    Zahl2 = Zahl1 + Zahl0 => 1 + 0 => 1
    Zahl3 = Zahl2 + Zahl1 => 1 + 1 => 2
    Zahl4 = Zahl3 + Zahl2 => 2 + 1 => 3
    ...
    Zahl10 = Zahl9 + Zahl8 => 34 + 21 => 55
    ...


## 1.2 Fibonacci Funktion
    ```python 
    {
        def fib1(n: int) -> int:
            if n < 2: # Abbruchbedingung
                return n
            return fib1(n-1) + fib1(n-2)
    }
    ```

# 1.2.1 Funktionsablauf.

    fib1(5) => fib1(4) + fib1(3) => 5
                
    fib1(4) => fib1(3) + fib1(2) => 3

    fib1(3) => fib1(2) + 1 => 2

    fib1(2) => fib1(1) + fib1(0) => 1

    fib1(2) => 1 + 0

    Start                                   fib1(4)
                                   
    Step1                   fib1(3)                                 fib1(2)

    Step2           fib1(2)             fib1(1)             fib1(1)            fib1(0)

    Step3       fib1(1)  fib1(0)            1                   1               0

    Step4           1       0

# 1.2.2 Anzahl der Aufrufe
fib(5) ->      5:     15
fib(9) ->     34:    109
fib(20) ->  6765:   21891
fib(25) -> 75025:  242785
