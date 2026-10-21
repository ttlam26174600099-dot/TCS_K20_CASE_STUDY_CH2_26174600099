# Bài 5. Nhập dữ liệu và chuyển đổi kiểu

# 17. Dùng input() để nhận bốn giá trị và in type() ngay sau khi nhập
ma_may = input("Nhập mã máy: ")
cong_suat_w_str = input("Nhập công suất W: ")
so_phut_str = input("Nhập số phút sử dụng: ")
don_gia_kwh_str = input("Nhập đơn giá điện/kWh: ")

print("\n--- KIỂU DỮ LIỆU BAN ĐẦU (str) ---")
print("mã máy:", type(ma_may))
print("công suất W:", type(cong_suat_w_str))
print("số phút:", type(so_phut_str))
print("đơn giá:", type(don_gia_kwh_str))

# 18. Chuyển đổi kiểu dữ liệu phù hợp
cong_suat_w = float(cong_suat_w_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_kwh_str)

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- KẾT QUẢ TÍNH TOÁN SAU KHI CHUYỂN ĐỔI KIỂU ---")
print("Điện năng tiêu thụ:", dien_nang_kwh, "kWh | Kiểu:", type(dien_nang_kwh))
print("Chi phí điện:", chi_phi, "VNĐ | Kiểu:", type(chi_phi))
