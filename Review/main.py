# B1: Nhi file input:
# input mấy dòng , mỗi dòng thì có bao nhiêu dữ liệu:
# 2 dòng, 3 dữ liệu

# for i in range(2): -> 2 dòng dữ liệu

# mỗi dòng 3 dữ liệu: a,b,c , dùng map để input
"""
file_input = open("CHUVI.INP","r")
file_output = open("CHUVI.OUT","w")
output = ""

for i in range(2): # 2 dòng dữ liệu
    a,b,c = map(int, file_input.readline().split()) # 3 biến 1 dòng
    # Chu vi tam giác:
    p = a + b + c # int
    output += str(p) + "\n"
file_output.write(output)
"""
"""
file_input = open("DIEMTB.INP","r")
file_output = open("DIEMTB.OUT","w")
output = ""
for i in range(2):
    a,b = map(int, file_input.readline().split())

    DTB = (a*3 + b) / 4 # 8.5
    if DTB >= 5:
        output += "1\n"
    else:
        output += "0\n"
file_output.write(output)
"""
"""
Input:
12 18
Output:
2 3
-> Rút gọn phan số:
B1: Tìm ước chung lớn nhất của tử số và mẫu số (6)
B2: Chia cả tử và mẫu cho UCLN (12 : 6 và 18 : 6)
-> 1 dòng, 1 dòng có 2 dữ liệu

UCLN 2 số l số lớn nhất mà a và b cùng chia hết

12: 1 2 3 4 [6] 12
18: 1 2 3 [6] 9 18
a<= b
"""
"""
file_input = open("RUTGON.INP","r")
file_output = open("RUTGON.OUT","w")
output = ""
# Vòng for thứ 2 không được dùng biến i:
for i in range(1):
    a,b = map(int, file_input.readline().split())
    ucln = 1
    for j in range(1,a+1):
        if a % j == 0 and b % j == 0:
            ucln = j
    # UCLN: 6
    # chia cả tử và mẫu số cho UCLN -> 2 3
    output += str(a // ucln) + " "
    output += str(b // ucln)
file_output.write(output)
"""

file_input = open("CAU1.INP","r")
file_output = open("CAU1.OUT","w")
output = ""
for i in range(2):
    n = int(file_input.readline())
    sum = 0
    for j in range(2,n+1):
        sum = sum + (j - 1) * j * (j + 1)
    # "\n"
    output += str(sum) +"\n"
file_output.write(output)





