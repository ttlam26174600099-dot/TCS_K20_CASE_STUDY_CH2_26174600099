tong_phut = 135
cong_suat_w = 250
#9
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("Số giờ trọn vẹn:", so_gio)
print("Số phút còn lại:", so_phut_con_lai)
#10
su_dung_lau = tong_phut > 60
print("Biến su_dung_lau:", su_dung_lau)
#11
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Biến du_lieu_hop_le:", du_lieu_hop_le)
#12
ket_qua_1 = 100 + 20 * 3
ket_qua_2 = (100 + 20) * 3
print("Kết quả biểu thức 1:", ket_qua_1)
print("Kết quả biểu thức 2:", ket_qua_2)
