coded_str=input("nhap chuoi: ")
word=coded_str.split(']')
print("danh sach sau khi tach:",word)
final=''
filter=[]
for item in word:
    if item.find('[')==-1:
        key=item
        value=1
        filter.append((key,value))
    else:
        part=item.split('[')
        key=part[1]
        value=int(part[0])
        filter.append((key,value))
        print(part)
for item in filter:
    if item[1]>1:
        final+=item[0]*item[1]
    else:
        final+=item[0]
print("chuoi sau khi giai ma:",final)