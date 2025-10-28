tong_tien = 0
so_mon = 0

print("--- CHƯƠNG TRÌNH QUẢN LÝ QUÁN CÀ PHÊ ---")
print("(Nhập 'x', 'skip', hoặc 'pass' ở tên món)")

while True:
    ten_mon = input("\nNhap ten mon: ").strip().lower()

    if ten_mon == "x":
        print("--- Đã kết thúc nhập món ---")
        break
    
    elif ten_mon == "skip":
        print("-> Bỏ qua (continue), mời nhập món tiếp theo.")
        continue 
    
    elif ten_mon == "pass":
        print("-> Giữ chỗ (pass), mời nhập món tiếp theo.")
        continue 
    gia_str = input(f"Nhap gia tien cho '{ten_mon}': ")
    try:
        gia_int = int(gia_str)
        
        if gia_int < 0:
            print("Gia phai la so duong! Bo qua mon nay.")
        else:
            print(f"-> Đã thêm: {ten_mon} - {gia_int}đ")
            tong_tien += gia_int
            so_mon += 1
            
    except ValueError:
        print("Gia tien khong hop le! Bo qua mon nay.")


print("\n========== HÓA ĐƠN ==========")
print("so mon:", so_mon)
print("Tong tien truoc khi giam: ", tong_tien)

if tong_tien > 200000:
    giam = tong_tien * 0.1
    tong_tien -= giam
    print("So tien giam: ", int(giam))
else:
    giam = 0
    print ("Khong duoc giam gia.")

print("Tong tien phai tra: ", int(tong_tien))