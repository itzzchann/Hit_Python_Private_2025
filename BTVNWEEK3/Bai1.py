n=int(input("Nhap so phan tu: "))
a=[]
for i in range(n):
    x=int(input("nhap phan tu thu {}:".format(i+1)))
    a.append(x)
print("Mang vua nhap la:",a)
limit=[]
seen=set()
for num in a:
    if num not in seen:
        seen.add(num)
        limit.append(num)
print("Mang sau khi loai bo phan tu trung la:",limit)
list1=[i**2 if i%2==0 else i**3 for i in limit] 
print("Mang sau khi bien doi la:",list1)
even_list=a[::2]
if len(even_list)>0:
    print("trung bình cộng các phần tử ở vị trí chẵn là:",sum(even_list)/len(even_list))
else:
    print("không có phần tử ở vị trí chẵn")
for i in range(len(limit)):
    swapped = False
    for j in range(0,len(limit)-i-1):
        if limit[j]>limit[j+1]:
            limit[j],limit[j+1]=limit[j+1],limit[j]
            swapped = True
    if not swapped:
        break
print("Mang sau khi sap xep la:",limit)