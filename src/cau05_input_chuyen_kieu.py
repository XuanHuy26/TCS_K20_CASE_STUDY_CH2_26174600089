ma_may = input("Nhap ma may: ")
print(type(ma_may))

cong_suat_W = float(input("Nhap cong suat W: "))
print(type(cong_suat_w))

so_phut = int(input("Nhap so phut: "))
print(type(so_phut))

don_gia_kwh = float(input("Nhap don gia: '))
print(type(don_gia_kwh))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang tieu thu (kwh):", dien_nang_kwh)
print("Chi phi (VND):", chi_phi)
