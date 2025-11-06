s="TV, Laptop, Phone, TV, Tablet, Laptop, Camera"
slist=s.split(', ')
slistset=set(slist)
final=tuple(slistset)
print("kho hàng(tuple):",final)
print("Tổng số loại hàng:",len(final))
listBanchay={"Phone", "Laptop", "Smartwatch"}
print("Sản phẩm bán chạy trong kho:",set(final).intersection(listBanchay))
print("Sản phẩm không nằm trong danh sách bán chạy:",set(final).difference(listBanchay))


