from math import gcd

def prob74(n):
    for i in range(8,n+1,2):
        p = 3
        q = 5
        if gcd(n-p,n-q) == 1:
            return{"result": f"Wszystkie liczby parzyste większe od 6 z danego zakresu zakończonego liczbą '{n}' spełniają zadany problem"}