print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - '10 diem'")
text = "CLB Tin Hoc HIT truc thuoc Khoa CNTT "
print("Chữ in hoa:", ''.join([c for c in text if c.isupper()]))
print("Chữ thường:", ''.join([c for c in text if c.islower()]))

if "CNTT" in text:
    print("YES")
else:
    print("NO")
print("đổi hoa sang thường", text.swapcase())