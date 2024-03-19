def them_muc_chieu():
    ten = input("Nhập tên mục chi tiêu: ")
    gia_tri = float(input("Nhập giá trị chi tiêu: "))
    ngay_chi = input("Nhập ngày chi (yyyy-mm-dd): ")
    muc_chieu = {'Tên': ten, 'Giá trị': gia_tri, 'Ngày chi': ngay_chi}
    danh_sach_muc_chieu.append(muc_chieu)
    print("Đã thêm thành công mục chi tiêu:", muc_chieu)

def xoa_muc_chieu():
    if len(danh_sach_muc_chieu) == 0:
        print("Danh sách mục chi tiêu rỗng.")
        return

    print("Danh sách mục chi tiêu:")
    for i, muc_chieu in enumerate(danh_sach_muc_chieu):
        print(f"{i+1}. Tên: {muc_chieu['Tên']}, Giá trị: {muc_chieu['Giá trị']}, Ngày chi: {muc_chieu['Ngày chi']}")

    index = input("Nhập số thứ tự mục chi tiêu để xoá: ")
    index = int(index) - 1

    if 0 <= index < len(danh_sach_muc_chieu):
        muc_chieu_bi_xoa = danh_sach_muc_chieu.pop(index)
        print("Đã xoá thành công mục chi tiêu:", muc_chieu_bi_xoa)
    else:
        print("Số thứ tự không hợp lệ.")

def in_danh_sach_muc_chieu():
    if len(danh_sach_muc_chieu) == 0:
        print("Danh sách mục chi tiêu rỗng.")
        return

    print("Danh sách mục chi tiêu:")
    for i, muc_chieu in enumerate(danh_sach_muc_chieu):
        print(f"{i+1}. Tên: {muc_chieu['Tên']}, Giá trị: {muc_chieu['Giá trị']}, Ngày chi: {muc_chieu['Ngày chi']}")

# Khởi tạo danh sách mục chi tiêu trống
danh_sach_muc_chieu = []

while True:
    print("===== Quản lý mục chi tiêu cá nhân =====")
    print("1. Thêm mục chi tiêu")
    print("2. Xoá mục chi tiêu")
    print("3. In danh sách mục chi tiêu")
    print("4. Thoát chương trình")

    lua_chon = input("Nhập lựa chọn của bạn (1-4): ")

    if lua_chon == '1':
        them_muc_chieu()
    elif lua_chon == '2':
        xoa_muc_chieu()
    elif lua_chon == '3':
        in_danh_sach_muc_chieu()
    elif lua_chon == '4':
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")