s=input("Nhap chuoi: ")
words=""
for char in s.lower():
    if char.isalpha() or char==" ":
        words+=char
word_list=words.split()
print("Danh sách các từ đã chuẩn hóa:",word_list)
unique=[]
count_word=[]
for word in word_list:
    if word not in unique:
        count_word.append((word,word_list.count(word)))
        unique.append(word)
print("Danh sách các từ không trùng lặp:",unique)
print("Số lần xuất hiện của từng từ:")
for item in count_word:
    print("{}: {}".format(item[0],item[1]))
max_tuple = max(count_word, key=lambda item: item[1])
max_len_tuple=max(count_word,key=lambda item: len(item[0]))
print("Từ xuất hiện nhiều nhất : '{}' - {} lần.".format(max_tuple[0],max_tuple[1]))
print("Từ dài nhất : '{}' - {} ký tự.".format(max_len_tuple[0],len(max_len_tuple[0])))
for i in range(len(unique)):
    swapped= False
    for j in range(0,len(unique)-i-1):
        if len(unique[j])>len(unique[j+1]):
            unique[j],unique[j+1]=unique[j+1],unique[j]
            swapped = True
    if not swapped:
        break
print("Danh sách các từ sau khi sắp xếp theo độ dài tăng dần:",unique)
