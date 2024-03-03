danh_sach=[6,8,2,9,1,7]

max =danh_sach[0]
min=danh_sach[0]
for i in  (danh_sach):
    if max <i:
        max=i
    if min>i:
        min=i

max2=danh_sach[0]
for i in danh_sach:
    if max2 <i and i <max:
        max2=i

print("Gia tri lon nhat ",max)
print("\nGia tri nho nhat ",min)

print(max2)