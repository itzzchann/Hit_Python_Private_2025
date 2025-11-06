s=input("nhap chuoi: ")
char_count={}
s1=s.lower()
for char in s1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)