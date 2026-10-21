from datetime import datetime

thoi-diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

# Giai thich su khac nhau[span_31](start_span)[span-31](end_span):
- datetime: Doi tuong chua thong tin day du ve ngay va gio, ho tro cac phep tinh toan thoi gian.
- str: Kieu chuoi van ban thuan tuy dung de hien thi hoac luu tru.
- timedelta: Khoang thoi gian (do lech) sinh ra khi thuc hien phep tru giua hai doi tuong datetime.
