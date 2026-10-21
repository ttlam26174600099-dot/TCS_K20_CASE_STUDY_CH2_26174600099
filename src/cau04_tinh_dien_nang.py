# Bài 4. Tính điện năng và chi phí

# Dữ liệu ban đầu
cong_suat_w = 250
don_gia_kwh = 3000

print("--- TRƯỜNG HỢP 1: so_phut = 90 ---")
so_phut = 90
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In giá trị và kiểu dữ liệu
print("Điện năng tiêu thụ:", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí điện:", chi_phi, "| Kiểu:", type(chi_phi))


print("\n--- TRƯỜNG HỢP 2: so_phut = 60 (Thay đổi theo yêu cầu 16) ---")
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In giá trị và kiểu dữ liệu sau khi thay đổi
print("Điện năng tiêu thụ mới:", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí điện mới:", chi_phi, "| Kiểu:", type(chi_phi))
