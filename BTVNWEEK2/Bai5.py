def cunghd(ngay,thang):
    if not (1<=thang<=12 and 1<=ngay<=31):
        return "Ngày hoặc tháng không hợp lệ!"
    if  thang in [4,6,9,11] and ngay>30:
        return "Ngày hoặc tháng không hợp lệ!"
    if thang==2 and ngay>29:
        return "Ngày hoặc tháng không hợp lệ!"
    chd=[
        ((1,20),"Cung hoang dao cua ban la: Bao Binh"),
        ((2,19),"Cung hoang dao cua ban la: Song Ngư"),
        ((3,21),"Cung hoang dao cua ban la: Bạch Dương"),
        ((4,20),"Cung hoang dao cua ban la: Kim Ngưu"),
        ((5,21),"Cung hoang dao cua ban la: Song Tử"),
        ((6,21),"Cung hoang dao cua ban la: Cự Giải"),
        ((7,23),"Cung hoang dao cua ban la: Sư Tử"),
        ((8,23),"Cung hoang dao cua ban la: Xử Nữ"),
        ((9,23),"Cung hoang dao cua ban la: Thiên Bình"),
        ((10,23),"Cung hoang dao cua ban la: Bọ Cạp"),
        ((11,22),"Cung hoang dao cua ban la: Nhân Mã"),
        ((12,22),"Cung hoang dao cua ban la: Ma Kết"),
    ]
    ngaysinh=(thang,ngay)
    for dk,ten in reversed(chd):
        if ngaysinh>=dk:
            return ten
    return "Cung hoang dao cua ban la: Ma Kết"
while True:
        ngay=int(input("nhap ngay sinh: "))
        thang=int(input("nhap thang sinh: "))
        ketqua=cunghd(ngay,thang)
        print(ketqua)
        while True:
            tieptuc=input("Ban co muon tiep tuc khong (y/n): ").strip().lower()
            if tieptuc=='y':
                break
            elif tieptuc=='n':
                print("Cam on ban da su dung chuong trinh!")
                exit()
            else:
                print("Vui long nhap y hoac n!")