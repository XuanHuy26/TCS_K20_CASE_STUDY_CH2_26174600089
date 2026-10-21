ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: ")) # Da sua loi thieu float()
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f} kwh")

# Loi goc: TyprError do bien cong_suat_w nhan chuoi (str) tu input nhung dem di nhan chia toan hoc.
# Cach sua: Ep kieu du lieu sang float cho cong_suat_w truoc khi tinh toan.
