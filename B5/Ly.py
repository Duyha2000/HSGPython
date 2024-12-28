"""
https://docs.google.com/document/d/1p9U0xzYb4hy27_hASj7rNvQDQ6JXQnWdOMtcEA0kY1w/edit?tab=t.0
Làm lại từ bài 1 bằng vòng lặp while
"""
"""
Bài tập 1: Hiển thị các số chẵn và tính tổng của chúng
Nhiệm vụ: Viết chương trình nhận một số nguyên n làm đầu vào, hiển thị tất cả các số chẵn từ n đến 100 và tính tổng của các số đó.
n = int(input()) # 90
while n <= 100:
    if n % 2 == 0:
        print(n ,end = " ")
    # step:
    n+=1
"""
"""
Bài tập 2: Số chia hết cho 3 và 5
Nhiệm vụ: Viết chương trình nhận hai số nguyên a và b làm đầu vào, hiển thị tất cả các số trong khoảng từ a đến b chia hết cho cả 3 và 5.
a = int(input())
b = int(input())
while a <= b :
    if a % 3 == 0 and a % 5 == 0 :
        print(a, end=" ")
    a+=1
"""
"""
Bài tập 3: Tính tổng các số từ 1 đến N
Nhiệm vụ: Viết chương trình tính tổng tất cả các số nguyên từ 1 đến N, với N là một số nguyên dương.
a=1
N=int(input()) # 10
sum = 0
while a <= N:
    sum+=a
    # step:
    a+=1

print(sum)
"""

# Bài toán tính tổng: sum = 0 -> sum = sum + i / a hoặc sum += i/a
# Bài toán tính tích: tich = 1 -> tich = tich * i/a hoặc tich *= i/a
# Bài toán đếm: count = 0 -> mỗi lần thỏa mãn điều kiện -> count += 1 hoặc count = count + 1
"""
Bài tập 4: Đếm các số chia hết cho X
Nhiệm vụ: Viết chương trình đếm xem có bao nhiêu số chia hết cho X trong khoảng từ A đến B, 
với A≤B và X là một số nguyên dương.
Ví dụ: Nếu A=1, B=50, và X=5, thì có 10 số chia hết cho 5: 5,10,15,…,50.
# Chưa đúng đâu em, trong while, em xem điều kiện chia hết đâu rồi:
count = 0
a = int(input()) # nhập X
b = int(input()) # Nhập A
x = int(input()) # Nhập B
while a <= b :
    # thiếu điều kiện:
    if a % x == 0 :
        count+=1
    # step
    a+= 1
print(count)
"""
"""
Bài tập 5: Tính tích các số từ 1 đến M
Nhiệm vụ: Viết chương trình tính tích của tất cả các số nguyên từ 1 đến M, với M là một số nguyên dương.
Lưu ý: Nếu M quá lớn, kết quả có thể vượt quá giới hạn kiểu dữ liệu.
tich = 1
a = 1
m = int(input())
while a <= m :
    tich *= a
    # step:
    a+=1
print(tich)
Bài tập 6: Đếm số ước
Nhiệm vụ: Viết chương trình nhập vào một số nguyên n và hiển thị số lượng ước của nó.
count = 0
a=1
n = int(input()) # 12:
# 12: chia hết cho những số nào từ 1 -> 12
while a <= n:
    if n % a == 0 :
        count+= 1
    # Step:
    a += 1
print(count)
Bài tập 7: Tính lũy thừa
Nhiệm vụ: Nhập vào hai số nguyên dương a và b, tính a^b ( a mũ b).
a = int(input())
b = int(input())
c = a**b
print(c)
Bài tập 8: Kiểm tra số nguyên tố:
Nhập 1 số và kiểm tra số đó có phải số nguyên tố hay không. 
Số nguyên tố là số chỉ chia hết cho 1 và chính nó ( số nguyên tố nhỏ nhất là số 2)
Ví dụ: 8 không phải số nguyên tố vì 8 chia hết cho 1 2 4 8 (ngoài chia hết cho 1 và 8 ra còn chia hết cho 2 và 4)
13 là số nguyên tố vì nó chỉ chia hết cho 1 và chính nó ( 1 và 13).
count = 0
a = 1
b = int(input())
while a <=b :
    if b % a == 0:
        count+=1
    # step:
    a += 1
# Nếu count = 2 -> thể hiện số đó chỉ chia hết cho 1 và chính số đó, thì nó là nguyên tố
if count == 2 :
     print("so nguyen to")
else :
     print ("khong phai so nguyen to")
Bài tập 9: Số nhỏ nhất chia hết cho 3, 5, và 7
Nhiệm vụ: Tìm số dương nhỏ nhất chia hết cho cả 3, 5, và 7
n = 1
# cho n = 1 -> tăng dần giá trị này -> đến khi bắt gặp số chia hết cho 3 5 7 thì in ra và thoát vòng lặp
while True:
    if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
        print(n, end=" ")
        break
    # step:
    n+=1
# In ra "3 số dương" chia hết cho 3 và 8
a = 1
count = 0
while True :
    if a % 3 == 0 and a % 8 == 0 :
        print(a,end=" ")
        count+= 1
    if count == 3:
        break
    # step:
    a+=1
# Tính tổng 10 số chẵn đầu tiên 
"""
count = 0
sum = 0
a = 1
while True:
    if a % 2 == 0:
       count+= 1
       sum+= a
    if count == 10 :
      break
    # Step:
    a+=1
# In ra tổng:
print(sum)