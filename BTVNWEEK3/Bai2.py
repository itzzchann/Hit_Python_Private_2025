s=input("Nhap chuoi: ")
words=""
for char in s.lower():
    if char.isalpha() or char==" ":
        words+=char
word_list=words.split()
clean=' '.join(word_list)
print("→ Chuẩn hóa:",clean)
clean=clean.replace(" ","")
key="ueoai"
count_vowel=sum( 1 for char in clean if char in key)
count_consonant=len(clean)-count_vowel
print("→ Nguyên âm:",count_vowel,"Phụ âm:",count_consonant)
words1=""
for char in s:
    if char.isalpha() or char==" ":
        words1+=char
word_list1=words1.split()
word_list_reverse=[word[::-1] for word in word_list1]
print("→ Đảo từng từ:",word_list_reverse)
is_palindrome = clean == clean[::-1]
print("→ Palindrome:",is_palindrome)