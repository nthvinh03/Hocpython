def get_product_info(products, product_id):
    if product_id in products:
        return products[product_id]
    else:
        return None

def update_product_list(products, product_id, new_name):
    products[product_id] = new_name

# Khởi tạo danh sách sản phẩm
products = {
    1: "Product A",
    2: "Product B",
    3: "Product C"
}

while True:
    # In ra các lựa chọn
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Sửa tên sản phẩm")
    print("4. Xoá sản phẩm")
    print("5. Thoát")
    
    # Nhập lựa chọn từ người dùng
    option = int(input("Chọn một chức năng (1-5): "))
    
    if option == 1:
        # Hiển thị danh sách sản phẩm
        print("Danh sách sản phẩm:")
        for product_id, product_name in products.items():
            print(f"{product_id}: {product_name}")
    
    elif option == 2:
        # Thêm sản phẩm mới
        product_id = int(input("Nhập ID sản phẩm: "))
        if get_product_info(products, product_id) is not None:
            print("Sản phẩm đã tồn tại với ID đã nhập.")
        else:
            product_name = input("Nhập tên sản phẩm: ")
            update_product_list(products, product_id, product_name)
            print("Thêm sản phẩm thành công.")
    
    elif option == 3:
        # Sửa tên sản phẩm
        product_id = int(input("Nhập ID sản phẩm cần sửa: "))
        product_info = get_product_info(products, product_id)
        if product_info is not None:
            new_name = input("Nhập tên mới cho sản phẩm: ")
            update_product_list(products, product_id, new_name)
            print("Cập nhật sản phẩm thành công.")
        else:
            print("Không tìm thấy sản phẩm với ID đã nhập.")
    
    elif option == 4:
        # Xoá sản phẩm
        product_id = int(input("Nhập ID sản phẩm cần xoá: "))
        product_info = get_product_info(products, product_id)
        if product_info is not None:
            del products[product_id]
            print("Xoá sản phẩm thành công.")
        else:
            print("Không tìm thấy sản phẩm với ID đã nhập.")
    
    elif option == 5:
        # Thoát khỏi chương trình
        break
    
    else:
        print("Lựa chọn không hợp lệ.")

# In ra danh sách sản phẩm sau khi quản lý
print("Danh sách sản phẩm sau khi quản lý:")
for product_id, product_name in products.items():
    print(f"{product_id}: {product_name}")