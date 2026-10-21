from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Bổ sung theo yêu cầu
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
```[cite: 9]

---

### **2. Dự đoán kết quả của phép trừ trước khi chạy (Câu 24)**[cite: 9]

* **Mốc thời gian bắt đầu (`bat_dau`):** Ngày 14/10/2026 lúc 13 giờ 15 phút[cite: 9].
* **Mốc thời gian kết thúc (`ket_thuc`):** Ngày 14/10/2026 lúc 15 giờ 05 phút[cite: 9].
* **Tính toán khoảng cách thời gian (`thoi_luong = ket_thuc - bat_dau`):**[cite: 9]
  * Từ 13:15 đến 14:00 là 45 phút[cite: 9].
  * Từ 14:00 đến 15:05 là 1 giờ 05 phút[cite: 9].
  * Tổng cộng khoảng thời gian chênh lệch là **1 giờ 50 phút**[cite: 9].
* **Dự đoán đầu ra hiển thị khi chạy:**[cite: 9]
  * Lệnh `print(thoi_luong)` sẽ cho kết quả: `1:50:00`[cite: 9].
  * Lệnh `print(type(thoi_luong))` sẽ cho kết quả kiểu dữ liệu: `<class 'datetime.timedelta'>`[cite: 9].

---

### **3. Giải thích sự khác nhau giữa `datetime`, `str` và `timedelta` (Câu 25)**[cite: 9]

* **`datetime`**: Là đối tượng biểu diễn một mốc thời gian cụ thể (bao gồm đầy đủ năm, tháng, ngày, giờ, phút, giây) do thư viện `datetime` quản lý, cho phép thực hiện các phép toán tính toán thời gian[cite: 9].
* **`str` (string)**: Là kiểu dữ liệu chuỗi ký tự văn bản thuần túy (được định dạng bằng hàm `strftime`)[cite: 9]. Kiểu `str` chỉ dùng để hiển thị hoặc in ra màn hình chứ không thể thực hiện trực tiếp các phép toán trừ ngày tháng[cite: 9].
* **`timedelta`**: Là đối tượng đại diện cho một khoảng thời gian (khoảng chênh lệch thời gian) sinh ra khi lấy một đối tượng `datetime` trừ đi một đối tượng `datetime` khác[cite: 9].
