"""
Bài 8. Số đặc biệt
Nhân một ngày nghỉ, Sơn ngồi học toán và nghĩ ra một số có tính chất đặc biệt: số chỉ có đúng 3 ước. Ví dụ số 25 có 3 ước là 1, 5, 25.
Yêu cầu: Cho số tự nhiên n (n < 109), hãy kiểm tra n có là số đặc biệt không?
Dữ liệu vào: Từ tệp văn bản SOHOC.INP chứa số n.
Kết quả: Đưa ra tệp văn bản SOHOC.OUT số 1 nếu n là số đặc biệt hoặc số 0 nếu n không là số đặc biệt.
Ví dụ:
SOHOC.INP
SOHOC.OUT
25
1


"""
file_input=open("SOHOC.INP","r")
file_output=open("SOHOC.OUT","w")
output=""
for i in range(1):
    n = int(file_input.readline())
    count = 0
    for j in range(1,n+1):
        if n % j == 0:
            count += 1
    if count == 3:
       output += "1\n"
    else:
        output += "0\n"
    # 0 - 1
    # count để đếm xem có bao nhiêu uoc, nếu = 3 ước thì đây là số đặc biệt
file_output.write(output)