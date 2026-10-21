# Bài 2. Biến và kiểu dữ liệu

# 5 & 6. Tạo các biến theo quy tắc snake_case và chọn kiểu dữ liệu phù hợp
ma_phien = "LAB026"         # str (chuỗi)
ma_may = "PC12"             # str (chuỗi)
cong_suat = 250.0           # float (số thực)
thoi_gian = 90              # int (số nguyên)
dang_hoat_dong = True       # bool (luận lý)
ghi_chu = None              # NoneType (không có giá trị)

# 7. In từng giá trị và dùng type() để kiểm tra kiểu
print("--- THÔNG TIN PHIÊN SỬ DỤNG BAN ĐẦU ---")
print("Mã phiên:", ma_phien, "| Kiểu:", type(ma_phien))
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))
print("Công suất:", cong_suat, "| Kiểu:", type(cong_suat))
print("Thời gian:", thoi_gian, "| Kiểu:", type(thoi_gian))
print("Đang hoạt động:", dang_hoat_dong, "| Kiểu:", type(dang_hoat_dong))
print("Ghi chú:", ghi_chu, "| Kiểu:", type(ghi_chu))

# 8. Thay thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian = 120
print("\n--- SAU KHI CẬP NHẬT THỜI GIAN ---")
print("Thời gian mới:", thoi_gian, "| Kiểu:", type(thoi_gian))
