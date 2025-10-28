def pro1(x,n):
    kq=1.0
    tmp=1.0
    for i in range(1,n+1):
        tmp*=x/i
        kq+=tmp
    return kq
def pro2(n):
    kq=1.0
    tmp=1.0
    for i in range(1,n+1):
        tmp/=i
        kq+=tmp
    return kq
x=float(input("Nhap x: "))
n=int(input("Nhap n: "))
print("Gia tri e^x theo cong thuc 1: ",pro1(x,n))
print("Gia tri e^x theo cong thuc 2: ",pro2(n))
      
   