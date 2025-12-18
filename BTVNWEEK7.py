#  Câu 1: In ra phiên bản của thư viện numpy đã cài đặt trong hệ thống
# import numpy as np

# print(np.__version__)


# from importlib_metadata import version
# print(version('numpy'))

# import pkg_resources
# print(pkg_resources.get_distribution('numpy').version)
# Câu 2:Tạo mảng 1 chiều từ 0 đến 20
import numpy as np
arr = np.arange(21)
print(arr)

# Câu 3: tạo mảng bolen 3x3  với các giá trị là true:
import numpy as np
arr  = np.ones((3,3),dtype = bool)
print(arr)

# câu 4:Lấy những phần tử mà thoả mãn một điều kiện cho trước của mảng một chiều
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)
arr_odd = arr[arr %2==1]
print(arr_odd)

# câu 5:Thay thế phần tử thoả mãn điều kiện cho trước bằng 1 một giá trị khác
import numpy as np
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)
arr[arr %2 ==1] = -1
print(arr)
# câu 6:    
# Thay thế tất cả số lẻ bằng giá trị -1 nhưng mảng ban đầu không thay đổi
import numpy as np
arr = np.arange(0, 10)
print(arr)
arr_new = np.where(arr % 2 != 0, -1, arr)
print(arr_new)
print(arr)
# câu 7:
import numpy as np

# tạo mảng 1d gồm 10 phần tử
arr = np.random.rand(10)
arr = np.arange(10)
print(arr)

# mảng 2 chiều có 2 hàng
arr_2d = arr.reshape(2, -1)
print(arr_2d)
# câu 10:
import numpy as np

# chỉ dùng hàm numpy có sẵn với mảng arr như bên dưới
arr = np.array([1,2,3])
print(arr)

# tạo mảng mới lặp lại mỗi phần tử trong arr 3 lần
arr_new = np.repeat(arr, 3)
print(arr_new)

# tạo mảng mới lặp lại mảng arr 3 lần
arr_new2 = np.tile(arr, 3)
print(arr_new2)

# tạo mảng mới lặp lại mảng arr 3 lần theo chiều ngang
arr_new3 = np.tile(arr, (1, 3))
print(arr_new3)
# câu 11:
import numpy as np

a = np.array([1,2,3,2,3,4,3,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Lấy phần tử chung của 2 mảng a và b
print(np.intersect1d(a, b))

# câu 12 : Xoá phần tử từ 1 mảng mà tồn tại trong 1 mảng khác

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# Từ mảng a xoá tất cả các phần tử ở a mà đã có trong mảng b
print(np.setdiff1d(a, b))

# câu 13:

import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Lấy tất cả vị trí nơi giá trị các phần tử của 2 mảng a,b giống nhau
print(np.where(a == b))

# câu 14 : Lấy tất cả các giá trị trong 1 phạm vi cho trước từ 1 mảng

import numpy as np

a = np.array([2,6,1,9,10,3,27])

# tìm tất cả các phần tử có giá trị trong phạm vi [5,10]
index = ((a >= 5) & (a <= 10))
print( a[index])

# câu 17 :  Hoán 2 hàng trong mảng 2 chiều

import numpy as np

# cho mảng arr có shape 3x3
arr = np.arange(9).reshape(3,3)
print(arr)

# Hoán dòng có index 0 và index 1 trong mảng arr
arr = arr[[1, 0, 2],:]
print(arr)


# câu 18 :

import numpy as np

# cho mảng arr có shape 3x3
arr = np.arange(9).reshape(3,3)
print(arr)
# Đảo ngược hàng (dòng) trong mảng 2 chiều
arr = arr[::-1,:]
print(arr)

#  Câu 20 :  Tạo mảng 2 chiều chứa số random kiểu float từ 5 đến 10
import numpy as np
# Tạo mảng 2 chiều 5x3 từ 5 đến 10
# Cách Dùng hàm random.uniform
arr = np.random.uniform(5, 10, (5, 3))
print(arr)