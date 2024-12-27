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
A=int(input())
B=int(input())
X=int(input())
count = 0
for i in range(A,B,1) :
    if i % X == 0:
        count+=1
print(count)
"""
"""
Bài tập 5: Tính tích các số từ 1 đến M
Nhiệm vụ: Viết chương trình tính tích của tất cả các số nguyên từ 1 đến M, với M là một số nguyên dương.
Lưu ý: Nếu M quá lớn, kết quả có thể vượt quá giới hạn kiểu dữ liệu.
Ví dụ: Nếu M=5M = 5M=5, tích là 1×2×3×4×5=1201
"""
"""
sum = 1
m = int(input())
for i in range(1,m+1,1):
    if i % 2 == 0:
       sum *= i
print(sum)
"""
"""
Bài tập 6: Đếm số ước
Nhiệm vụ: Viết chương trình nhập vào một số nguyên n và hiển thị số lượng ước của nó.
Các bước:
Nhập vào số nguyên n.
Lặp qua các số từ 1 đến n.
Kiểm tra nếu số đó chia hết cho n.
Đếm và in ra số lượng ước.
Ví dụ: Với n = 12, có 6 ước: 1,2,3,4,6,12.
"""
"""
count = 0
n = int(input())
for i in range(1,n,1):
    if n % i == 0:
        count += 1
print(count)
"""
"""
Bài tập 7: Tính lũy thừa
Nhiệm vụ: Nhập vào hai số nguyên dương a và b, tính a^b.
Các bước:
Nhập vào hai số nguyên a và b.
Dùng vòng lặp hoặc toán tử * để tính a^b.
In kết quả.
Ví dụ: Với a = 2 và b = 3, kết quả là 2^3 = 8.
"""
"""
a = int(input())
b = int(input())
p = a**b
print(p)
"""
"""
 Bài tập: Nhập 1 số và kiểm tra số đó có phải số hoàn hảo hay ko?
Số hoàn hảo là số mà tổng các ước thực sự của nó (không tính chính nó) bằng chính nó.
Ví dụ: N = 28 có các ước 1, 2, 4, 7, 14, 28 thì các ước thực sự là 1, 2, 4, 7, 14
có tổng cũng bằng 28 nên 28 là số hoàn hảo

Gợi ý: Nhập N -> Tính tổng các ước của số đó:
sum =  0
N = int(input())
for i in range(1,N):
    if N % i == 0:
        sum+= i
# Nếu số n nhập vào = sum, thì đây là số hoàn hảo, còn không thì in ra không phải số hoàn hảo
if N == sum :
    print("số hoàn hảo")
else:
    print("số không hoàn hảo")

Bài tập: Nhập vào 1 số và kiểm tra số đó có phải số nguyên tố hay ko.
Số nguyên tố là số chỉ chia hết cho 1 và chính nó ( số nguyên tố 
nhỏ nhất là số 2)
13 -> là số nguyên tố (vì chỉ chia hết cho 1 và 13)
8 -> ko phải nguyên tố vì nó chia hết cho (1 2 4 và 8)
Gợi ý: sử dụng biến count (vì số nguyên tố chỉ chia hết cho 2 số nên count = 2, số không phải nguyên tố chia hết cho nhiều hơn 2 số)
# a = int(input()) # a = 13

# 13 chỉ chia hết cho 1 và 13 ( 2 số)
# 11 chia hết cho 1 và 11 ( 2 số )
# Số nguyên tố là số chỉ hết cho 1 và chính no ( 2 số )
# 8 chi hết cho 1 2 4 8 (4 số)
# 6 chia hết cho 1 2 3 6 ( 4 số) -> chia hết nhiều hơn 2 số
count = 0
for i in range(1,a+1):
    if a % i ==0:
        count+=1
if count ==2:
    print("Nguyen to")
else:
    print("Ko phai nguyen to")
"""

"""
Bài tập: In ra các số: 1 2 4 5 6 7 9 10 bằng vòng lặp for
Sử dụng if và != để loại bỏ số 3 và 8
"""
"""
For if cuối dòng có :
if, for phải tab vào lề 1 lần
"""
"""
for i in range (1,11):
    if i != 3 and i != 8:
        print(i)

# Continue: bỏ qua giá trị:
for i in range(1,11):
    if i == 3 or i == 8:
        continue
    print(i, end=" ")
"""
"""
print()
# In ra các số chẵn (nghĩa là bỏ qua các số lẻ) từ 1 đến 10 sử dụng continue
for i in range(1,11):
    if i%2 != 0 :
        continue
    print(i, end="")
print()
# break: thoát vòng lặp:
# In ra  số đầu tiên chia hết cho 3 trong đoạn từ 1 đến 30

for i in range(1,31,1):
    if i % 3 == 0:
        print(i, end=" ")
        break
"""
# In ra 3 số đầu tiên: chia hết cho 3 và 5 trong đoạn từ 1 đến 200:
# Gợi ý: dùng count, for và break
count = 0
for i in range(1,201,1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
        count+=1
    if count == 3:
        break

