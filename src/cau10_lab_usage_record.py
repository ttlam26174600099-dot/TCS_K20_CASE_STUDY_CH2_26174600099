from datetime import datetime

# Nhập các thông tin từ người dùng
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w_str = input("Nhập công suất thiết bị (W): ")
so_phut_str = input("Nhập thời gian sử dụng (phút): ")
don_gia_str = input("Nhập đơn giá điện (VND/kWh): ")

# Chuyển đổi kiểu dữ liệu phù hợp
cong_suat_w = float(cong_suat_w_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

# Tính toán điện năng tiêu thụ và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Kiểm tra điều kiện trên 60 phút (trả về True/False, không dùng if)
tren_60_phut = so_phut > 60

# Lấy thời điểm ghi nhận hiện tại và định dạng chuỗi
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# In kết quả theo đúng định dạng mẫu yêu cầu
print("\n--- KẾT QUẢ GHI NHẬN PHIÊN SỬ DỤNG ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")
```[cite: 10]

---

### **4. Kiểm thử chương trình với bộ dữ liệu mẫu**[cite: 10]
* **Dữ liệu nhập vào:** 
  * Mã phiên: `LAB026`[cite: 10]
  * Mã máy: `PC12`[cite: 10]
  * Công suất: `250`[cite: 10]
  * Số phút: `90`[cite: 10]
  * Đơn giá: `3000`[cite: 10]

* **Đầu ra (Output) hiển thị:**[cite: 10]
  ```text
  Mã phiên: LAB026
  Máy: PC12
  Công suất: 250.00 W
  Thời lượng: 90 phút
  Điện năng: 0.375 kWh
  Chi phí: 1125.00 VND
  Trên 60 phút: True
  Ghi nhận lúc: 2026-10-21 21:00:00  (Ví dụ thời điểm hệ thống hiện tại)
  ```[cite: 10]
