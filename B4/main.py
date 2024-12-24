"""
Bài tập 1: Hiển thị các số chẵn và tính tổng của chúng
Nhiệm vụ: Viết chương trình nhận một số nguyên n làm đầu vào, hiển thị tất cả các số chẵn từ n đến 100 và tính tổng của các số đó.
Các bước:
Nhập vào số nguyên n.
Lặp qua các số từ n đến 100.
Kiểm tra nếu số đó là số chẵn (chia hết cho 2).
In ra các số chẵn.
Tính và hiển thị tổng của các số chẵn.
Đầu vào: Số nguyên n (ví dụ: 90).
Đầu ra:
Tất cả các số chẵn từ n đến 100 (ví dụ: 90 92 94 96 98 100).
Tổng của các số chẵn (ví dụ: Tổng = 570).
"""
"""
sum = 0
for i in  range (2,101,1):
    if i %2 == 0  :
        sum = sum + i
print (sum)
"""
"""
Bài tập 2: Số chia hết cho 3 và 5
Nhiệm vụ: Viết chương trình nhận hai số nguyên a và b làm đầu vào, hiển thị tất cả các số trong khoảng từ a đến b chia hết cho cả 3 và 5.
Các bước:
Nhập hai số nguyên a và b.
Lặp qua các số từ a đến b.
Kiểm tra nếu số đó chia hết cho cả 3 và 5.
In ra các số hợp lệ.
Đầu vào: Hai số nguyên a và b (ví dụ: 1 và 50).
Đầu ra: Tất cả các số chia hết cho cả 3 và 5 (ví dụ: 15 30 45).
"""
"""
a = int(input())
b = int(input())
# i tăng dần từ a đến b
for i in range (a,b+1,1) :
    if i % 3 == 0 and i % 5== 0:
        print(i)
"""
"""
Bài tập 3: Tính tổng các số từ 1 đến N
Nhiệm vụ: Viết chương trình tính tổng tất cả các số nguyên từ 1 đến N, với N là một số nguyên dương.
Ví dụ: Nếu N = 10, tổng là 1+2+3+⋯+10=55
sum = 0
N = int(input())
# Nhập N đi em, 1000 ở đâu ra đó
for i in range(1,N,1):
    sum+= i
print(sum)

Bài tập 4: Đếm các số chia hết cho X
Nhiệm vụ: Viết chương trình đếm xem có bao nhiêu số chia hết cho X trong khoảng từ A đến B,
với A ≤B  và X là một số nguyên dương.
Ví dụ: Nếu A = 1, B = 50, và X = 5, thì có 10 số chia hết
-> 5 10 15 20 25 30 35 40 45 50 ( 10 số thỏa mãn)
"""
A=int(input())
B=int(input())
X=int(input())
count = 0
for i in range(A,B,1) :
    if i % X == 0:
        count+=1
print(sum)