# src/cau07_chan_doan_loi.py

ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Sửa lỗi kiểu dữ liệu (TypeError): ép sang float
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")     # Sửa lỗi tên biến (NameError): dùng đúng biến dien_nang_kwh

# Lỗi 1 (TypeError): cong_suat_w nhận giá trị từ input() là chuỗi (str), cần ép kiểu float trước khi tính toán.
# Lỗi 2 (NameError): Gọi sai tên biến dien_nang trong hàm print() thay vì dùng biến đúng là dien_nang_kwh.


