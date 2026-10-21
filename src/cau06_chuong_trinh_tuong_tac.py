# Bài 6. Chương trình tương tác hoàn chỉnh

# 1. Nhập dữ liệu từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_str = input("Nhập công suất (W): ")
so_phut_str = input("Nhập số phút sử dụng: ")
don_gia_str = input("Nhập đơn giá điện/kWh: ")

# 2. Chuyển đổi kiểu dữ liệu phù hợp
cong_suat = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia = float(don_gia_str)

# 3. Tính toán điện năng và chi phí
dien_nang = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang * don_gia

# 4. In kết quả theo đúng định dạng yêu cầu
print("\n--- THÔNG TIN KẾT QUẢ ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang}")
print(f"Chi phí: {chi_phi}")
