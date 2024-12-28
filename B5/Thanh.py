"""
https://docs.google.com/document/d/1p9U0xzYb4hy27_hASj7rNvQDQ6JXQnWdOMtcEA0kY1w/edit?tab=t.0
Làm lại từ bài 1 bằng vòng lặp while

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
Tổng của các số chẵn (ví dụ: Tổng = 570)
n = int(input()) # 90
while n <= 100:
    if n % 2 == 0:
        print(n, end=" ")
    # Step: bước nhay:
    n+=1
"""
"""
Bài tập 2: Số chia hết cho 3 và 5
Nhiệm vụ: Viết chương trình nhận hai số nguyên a và b làm đầu vào, 
hiển thị tất cả các số trong khoảng từ a đến b chia hết cho cả 3 và 5.
Các bước:
Nhập hai số nguyên a và b.
Lặp qua các số từ a đến b.
Kiểm tra nếu số đó chia hết cho cả 3 và 5.
In ra các số hợp lệ.
Đầu vào: Hai số nguyên a và b (ví dụ: 1 và 50).
Đầu ra: Tất cả các số chia hết cho cả 3 và 5 (ví dụ: 15 30 45)
a = int(input()) # a = 1
b = int(input()) # b = 50
while a <= b :
    if a % 3 ==0 and a % 5 == 0:
        print(a, end=" ")
    # step:
    a+=1
"""
"""
Bài tập 3: Tính tổng các số từ 1 đến N
Nhiệm vụ: Viết chương trình tính tổng tất cả các số nguyên từ 1 đến N, với N là một số nguyên dương.
Ví dụ: Nếu N = 10, tổng là 1+2+3+⋯+10=551 + 2 + 3 + \dots + 10 = 551+2+3+⋯+10=55.
a = 1
n = int(input()) # n = 10
sum = 0
# sum = 0 -> sum = sum +
while a <= 10:
   sum = sum + a
   a+=1
print(sum)
"""

# Bài toán tính tổng: sum = 0 -> sum = sum + i / a hoặc sum += i/a
# Bài toán tính tích: tich = 1 -> tich = tich * i/a hoặc tich *= i/a
# Bài toán đếm: count = 0 -> mỗi lần thỏa mãn điều kiện trong if else -> count += 1 hoặc count = count + 1
"""
Bài tập 4: Đếm các số chia hết cho X
Nhiệm vụ: Viết chương trình đếm xem có bao nhiêu số chia hết cho X trong khoảng từ A đến B, 
với A≤B và X là một số nguyên dương.
Ví dụ: Nếu A=1, B=50, và X=5, thì có 10 số chia hết cho 5: 5,10,15,…,50.
count = 0
a = int(input())
b = int(input())
x = int(input())
while a <= b:
   if a % x == 0:
      count+=1
   # step
   a += 1
# in trong vòng lặp
print(count)
"""
"""
Bài tập 5: Tính tích các số từ 1 đến M
Nhiệm vụ: Viết chương trình tính tích của tất cả các số nguyên từ 1 đến M, 
với M là một số nguyên dương.
Lưu ý: Nếu M quá lớn, kết quả có thể vượt quá giới hạn kiểu dữ liệu.
Ví dụ: Nếu M=5M = 5M=5, tích là 1×2×3×4×5=1201 
\times 2 \times 3 \times 4 \times 5 = 1201×2×3×4×5=120.
tich = 1
a = 1
m = int(input())
while m <= a:
   # bài này không bắt kiểm tra số chẵn
   tich = tich * m
   m+=1
print(tich)
"""
"""
Bài tập 6: Đếm số ước
Nhiệm vụ: Viết chương trình nhập vào một số nguyên n và hiển thị số lượng ước của nó.
Các bước:
Nhập vào số nguyên n.
Lặp qua các số từ 1 đến n.
Kiểm tra nếu số đó chia hết cho n.
Đếm và in ra số lượng ước.
Ví dụ: Với n = 12, có 6 ước: 1,2,3,4,6,121, 2, 3, 4, 6, 121,2,3,4,6,12.

count = 0
a = 1
n = int(input()) # 12
# 12: chia hết cho những số nào từ 1 -> 12
while a <= n:
   if n % a == 0:
      count = count + 1
   # step:
   a+=1
print(count)
"""
"""
Bài tập 7: Tính lũy thừa
Nhiệm vụ: Nhập vào hai số nguyên dương a và b, tính aba^bab.
Các bước:
Nhập vào hai số nguyên a và b.
Dùng vòng lặp hoặc toán tử * để tính aba^bab.
In kết quả.
Ví dụ: Với a = 2 và b = 3, kết quả là 23=82^3 = 823=8

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
n = int(input()) # 13
while a <= n:
   # Thỏa mãn 1 điều kiện count mới tăng:
   if n % a == 0:
    count = count + 1
   # step:
   a+=1
if count == 2:
   print("là số nguyên tố")
else:
   print("không phải số nguyên tố")

Bài tập 9: Số nhỏ nhất chia hết cho 3, 5, và 7
Nhiệm vụ: Tìm số dương nhỏ nhất chia hết cho cả 3, 5, và 7.
Các bước:
1Khởi tạo biến n = 1.
2Dùng vòng lặp kiểm tra tính chia hết của n với 3, 5, và 7.
3Dừng lại khi tìm được số thỏa mãn.
In kết quả.
Ví dụ: Số nhỏ nhất chia hết cho 3, 5, và 7 là 105.


# In ra "3 số dương" chia hết cho 3 và 8
n = 1
count = 0 # count -> ??
while True :
   if n % 3 ==0 and n % 8 == 0:
      print(n, end=" ")
      count+=1
   # Khi nào thoát vòng lặp   bre
   if count == 3:
      break
   #step:
   n +=1
"""
# Tính tổng 10 số chẵn đầu tiên
n = 1
count = 0
sum = 0
while True :
   if n % 2 == 0:
      sum = sum + n
      count = count + 1
   if count == 10:
      break
   # Khi nào thoát vòng lặp:
   #step:
   n +=1
# In ra tổng:
print(sum)