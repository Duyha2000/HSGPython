# https://docs.google.com/document/d/1eWziDxM5O-3bnIJvfN3qTZAKeMF-Mvm6ny8z_by9Po4/edit?tab=t.0#heading=h.cafut2r9m0va
# https://meet.google.com/bmt-zwjc-xos
"""
Bài 10:
Kiểm tra điều kiện tốt nghiệp của sinh viên
Viết chương trình kiểm tra xem sinh viên có đủ điều kiện tốt nghiệp hay không, với các điều kiện sau:
Sinh viên đang theo học khóa "UG" (đại học không danh dự) cần hoàn thành 72 tín chỉ trở lên.
Sinh viên đang theo học khóa "UG (Hons)" (đại học danh dự) cần hoàn thành 96 tín chỉ trở lên.
Sinh viên đang theo học khóa "PG" (sau đại học) cần hoàn thành 48 tín chỉ trở lên.

***Dữ liệu đầu vào***:
course: Kiểu str. Một trong các giá trị: "UG", "UG (Hons)", hoặc "PG".
credit_points: Kiểu int. Số tín chỉ đã hoàn thành.

Dùng toán tử and,or và if - elif -else

course = input() # Khóa học
credit_points = int(input()) # số tin chỉ

if course == "UG" and credit_points >= 72:
    print("đại học không danh dự")
elif course == "UG(Hons)" and credit_points >= 96:
    print("đại học danh dự ")
elif course == "PG" and credit_points >= 48:
    print("sau đại học")
else:
    print("rớt ")


Bài 12:
Tính phí đỗ xe dựa trên thời gian đỗ
Quy tắc tính phí:
< 3 giờ: Miễn phí.
3 giờ - 3 giờ 29 phút: $4. and - or
3 giờ 30 phút - 3 giờ 59 phút: $7.
4 giờ - 4 giờ 29 phút: $11.
4 giờ 30 phút - 4 giờ 59 phút: $16.
5 giờ - 5 giờ 29 phút: $22.
5 giờ 30 phút - 5 giờ 59 phút: $30.
> 6 giờ: $40.
Dữ liệu đầu vào:
hours: Kiểu int. Số giờ đỗ.
minutes: Kiểu int. Số phút đỗ.
Yêu cầu:
Tính phí đỗ xe và lưu vào biến parkingFee.c
"""
hours = int(input())  # 2
minutes = int(input()) # 30
## Đổi hết sang phút đi:
tongsophut = hours * 60 + minutes
if tongsophut < 180 :
    print("miễn phí")
elif 180 < tongsophut < 209:
    print("$4")
elif 210 < tongsophut < 239:
    print("$7")
elif 240 < tongsophut < 269:
    print("$11")
elif 270 < tongsophut < 299:
    print("$16")
elif 300 < tongsophut < 329:
    print("$22")
elif 330 < tongsophut < 359:
    print("$30")
else:
    print("$40")