file_input=open("UOCNT.INP","r")
file_output=open("UOCNT.OUT","w")
output = ""


for i in range(1):
    a = int(file_input.readline())
    count = 0
    for j in range(1,a + 1):
        if a % j == 0:
            countnto = 0
            for k in range(1,j+1):
                if j % k == 0:
                    countnto += 1
            if countnto == 2:
                count +=1
    output = str(count)
file_output.write(output)
"""
Khung làm bài tin học:
B1: Mở file input và output
file_input = open("DIEMTB.INP","r")
file_output = open("DIEMTB.OUT","w")
output = ""
B2: Đọc input xem có mấy dòng, mỗi dòng có bao nhiêu dữ kiện
Nếu 2 dòng: for i in range(2) 
         Nếu 1 dữ kiện: a = int(file_input.readline())
         Nếu nhiều dữ kiện: a,b = map(int, file_input.readline().split())
B3: file_output.write(output)
*** Lưu ý: 
+ Vòng for bên trong: for j, k (không dùng chung tên biến i)
+ Bài toán tính tổng: khởi tạo biến tong = 0 --> tong = tong + ... ( hoặc tong += ...)
+ Bài toán tính tích: khởi tạo biến tich = 1 --> tich = tich * ... ( hoặc tich *= ...)
+ Bài toán đếm: khởi tạo biến dem = 0 -> Mỗi lần thỏa mãn: count += 1
"""