data=input("Nhap du lieu: ")
filter=[]
pairs=data.split(",")
for pair in pairs:
    part=pair.strip().split(":")
    key=part[0]
    value=float(part[1])
    filter.append((key,value))
print("Chuan hoa:")
for item in filter:
    print("{}: {}".format(item[0],item[1]))
name=set()
for item in filter:
    name.add(item[0])
average_list=[]
for n in name:
    total=0
    count=0
    for item in filter:
        if item[0]==n:
            total+=item[1]
            count+=1
    average=total/count
    average_list.append((n,average))
print("Diem trung binh cua tung sinh vien:")
for item in average_list:
    print("{} - {:.2f}".format(item[0],item[1]))
max_avg=max(average_list,key=lambda item:item[1])
min_avg=min(average_list,key=lambda item:item[1])
print("Sinh vien co diem trung binh cao nhat: {} - {:.2f}".format(max_avg[0],max_avg[1]))
print("Sinh vien co diem trung binh thap nhat: {} - {:.2f}".format(min_avg[0],min_avg[1]))
n=len(average_list)
for i in range(n):
    swapped=False
    for j in range(0,n-i-1):
        if average_list[j][1]<average_list[j+1][1]:
            average_list[j],average_list[j+1]=average_list[j+1],average_list[j]
            swapped=True
    if not swapped:
        break
print("Danh sach sinh vien theo diem trung binh tang dan:",average_list)


