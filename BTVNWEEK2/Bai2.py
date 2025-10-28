import math

def uocle(n):
    if n <= 2:
        return 0
    return int(math.sqrt(n - 1)) - 1
n=int(input("Nhap n: "))
print(uocle(n))  