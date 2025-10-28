s= input("Nhap chuoi: ")
at=s.find('@')
dot=s.find('.')
if at>0 and dot>at+1 and dot<len(s)-1:
    print("Valid")
else:
    print("Invalid")