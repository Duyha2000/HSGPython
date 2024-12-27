"""
https://docs.google.com/document/d/1p9U0xzYb4hy27_hASj7rNvQDQ6JXQnWdOMtcEA0kY1w/edit?tab=t.0

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


Bài tập 2: Số chia hết cho 3 và 5
Nhiệm vụ: Viết chương trình nhận hai số nguyên a và b làm đầu vào, hiển thị tất cả các số trong
 khoảng từ a đến b chia hết cho cả 3 và 5.
Các bước:
Nhập hai số nguyên a và b.
Lặp qua các số từ a đến b.
Kiểm tra nếu số đó chia hết cho cả 3 và 5.
In ra các số hợp lệ.
Đầu vào: Hai số nguyên a và b (ví dụ: 1 và 50).
Đầu ra: Tất cả các số chia hết cho cả 3 và 5 (ví dụ: 15 30 45).

Bài tập 3: Tính tổng các số từ 1 đến N
Nhiệm vụ: Viết chương trình tính tổng tất cả các số nguyên từ 1 đến N, với N là một số nguyên dương.
Ví dụ: Nếu N = 10, tổng là 1+2+3+⋯+10=55

Bài tập 4: Đếm các số chia hết cho X
Nhiệm vụ: Viết chương trình đếm xem có bao nhiêu số chia hết cho X trong khoảng từ A đến B,
 với A≤B và X là một số nguyên dương.
Ví dụ: Nếu A=1, B=50, và X=5, thì có 10 số chia hết
-> 5 10 15 20 25 30 35 40 45 50 ( 10 số thỏa mãn)

Bài tập 5: Tính tích các số chẵn từ 1 đến M
Nhiệm vụ: Viết chương trình tính tích của tất cả các số nguyên từ 1 đến M,
với M là một số nguyên dương.
Ví dụ: Nếu M=5, tích là 2 * 4 = 8

Bài tập 6: Đếm số ước
Nhiệm vụ: Viết chương trình nhập vào một số nguyên n và hiển thị số lượng ước của nó.
Các bước:
Nhập vào số nguyên n.
Lặp qua các số từ 1 đến n.
Kiểm tra nếu số đó chia hết cho n.
Đếm và in ra số lượng ước.
Ví dụ: Với n = 12, có 6 ước: 1,2,3,4,6,12.

Bài tập 7: Tính lũy thừa
Nhiệm vụ: Nhập vào hai số nguyên dương a và b, tính a^b.
Các bước:
Nhập vào hai số nguyên a và b.
Dùng vòng lặp hoặc toán tử * để tính a^b.
In kết quả.
Ví dụ: Với a = 2 và b = 3, kết quả là 2^3 = 8.

Bài tập 8: Đếm số chia hết cho X
Nhiệm vụ: Viết chương trình nhận ba số nguyên A, B, và X (A<BA < BA<B),
 đếm bao nhiêu số trong khoảng từ A đến B (bao gồm cả A, B) chia hết cho X.
Ví dụ: Với A=1,B=10,X=2, có 5 số chia hết cho 2: 2,4,6,8,10.

Bài tập 9: Số nhỏ nhất chia hết cho 3, 5, và 7
Nhiệm vụ: Tìm số dương nhỏ nhất chia hết cho cả 3, 5, và 7.
Các bước:
Khởi tạo biến n = 1.
Dùng vòng lặp kiểm tra tính chia hết của n với 3, 5, và 7.
Dừng lại khi tìm được số thỏa mãn.
In kết quả.
Ví dụ: Số nhỏ nhất chia hết cho 3, 5, và 7 là 105.

Bài tập 10: Máy tính hình học
Nhiệm vụ: Phát triển chương trình tính chu vi và diện tích các hình dựa trên menu lựa chọn.
Menu:
Tính chu vi và diện tích hình chữ nhật.
Tính chu vi và diện tích hình tam giác.
Tính chu vi và diện tích hình tròn.
Thoát.
Các bước:
Hiển thị menu cho người dùng.
Nhập lựa chọn của người dùng.
Dựa trên lựa chọn, nhập các kích thước liên quan (ví dụ: bán kính, cạnh).
Tính toán và hiển thị kết quả.
Lặp lại cho đến khi người dùng chọn thoát.

Bài tập 11: Menu đồ uống
Nhiệm vụ: Viết chương trình hiển thị menu đồ uống và cho phép người dùng chọn:
Menu:
Coke: Giá $1.25.
Pepsi: Giá $1.00.
Nước lọc: Giá $2.00.
Cà phê: Giá $1.50.
Thoát.
Yêu cầu:
Hiển thị menu và cho phép người dùng nhập lựa chọn.
Xử lý các trường hợp:
Nếu chọn 1-4: Hiển thị đồ uống đã chọn và giá.
Nếu chọn 5: Thoát và hiển thị thông báo "Tạm biệt!".
Nếu nhập sai: Hiển thị "Lựa chọn không hợp lệ" và yêu cầu nhập lại.
Lặp lại cho đến khi người dùng chọn thoát.

Bài tập 12: Máy tính
Nhiệm vụ: Viết chương trình hiển thị menu các phép toán cơ bản và cho phép người dùng thực hiện tính toán.
Menu:
Cộng.
Trừ.
Nhân.
Chia.
Thoát.
Yêu cầu:
Nhập lựa chọn và hai số.
Thực hiện phép toán tương ứng:
Nếu chọn 4 (chia): Hiển thị lỗi nếu mẫu số bằng 0.
Nếu nhập sai lựa chọn: Hiển thị "Lựa chọn không hợp lệ".
Lặp lại cho đến khi chọn thoát.

Bài tập 13: Kiểm tra đầu vào
Nhiệm vụ: Viết chương trình kiểm tra đầu vào tuổi hợp lệ. Tuổi phải nằm trong khoảng từ 0 đến 120.
Yêu cầu:
Nhập tuổi từ người dùng.
Kiểm tra nếu tuổi không hợp lệ:
Hiển thị "Tuổi không hợp lệ. Nhập lại".
Yêu cầu nhập lại.
Khi nhập hợp lệ, hiển thị "Tuổi đã được ghi nhận: [tuổi]".

Bài tập 14: Trò chơi đoán số
Nhiệm vụ: Viết chương trình trò chơi đoán số:
Chọn ngẫu nhiên một số từ 1 đến 100.
Người chơi nhập dự đoán nhiều lần cho đến khi đúng.
Hiển thị gợi ý "Quá cao!" hoặc "Quá thấp!" sau mỗi lần đoán.
Mở rộng: Đếm số lần đoán và hiển thị khi người chơi thắng.
"""
#bài 1
"""
sum = 0
n = int(input())
for i in range(n,101,1):
    if i % 2 == 0:
        sum = sum + i
print(sum)
For, if khi xuống dòng tab vào 1 lần, trên dòng thì sẽ có :
Bài 2:
a = int(input())
b = int(input())
# Giá trị: i đi từ 1 -> 50
for i in range(a,b + 1 ,1 ):
    if i % 3 == 0 and i % 5 == 0:
        print(i) # 15 30 45
Bài 3:
sum = 0
n = int(input())
for i in range(1,n+1,1):
      sum = sum +i
print(sum)
Bài 4:
count  = 0
a = int(input())
b = int(input())
x = int(input())

for i in range(a,b +1,1):
    if i % x == 0:
        count+= 1
print(count) # 5 - 10
Bài 5:
tich = 1
m = int(input())
for i in range(1,m+1,1):
    if i % 2 == 0:
       tich = tich * i
print(tich)
count = 0
n = int(input()) # 12
# i đi từ 1 -> 12
# 1 2 3 4 6 12 vì 12 chia hết cho những số này:
for i in range(1,n+1,1):
    if n % i == 0:
        count += 1
print(count)
bài 7:
a = int(input())
b = int(input())
print(a**b)sum
"""
"""
Bài tập: Nhập 1 số và kiểm tra số đó có phải số hoàn hảo hay ko?
Số hoàn hảo là số mà tổng các ước thực sự của nó (không tính chính nó) bằng chính nó.
Ví dụ: N = 28 có các ước 1, 2, 4, 7, 14, 28 thì các ước thực sự là 1, 2, 4, 7, 14
có tổng cũng bằng 28 nên 28 là số hoàn hảo
Gợi ý: Nhập N -> Tính tổng các ước của số đó:
sum = 0
n = int(input())
for i in range(1,n,1):
    if n % i == 0:
        sum = sum + i
# Nếu số n nhập vào = sum, thì đây là số hoàn hảo, còn không thì in ra không phải số hoàn hảo
if n == sum:
    print("số hoàn hảo")
else:
    print("không phải só hoàn hảo")

Bài tập: Nhập vào 1 số và kiểm tra số đó có phải số nguyên tố hay ko. 
Số nguyên tố là số chỉ chia hết cho 1 và chính nó ( số nguyên tố nhỏ nhất là số 2)
13 -> là số nguyên tố (vì chỉ chia hết cho 1 và 13)
8 -> ko phải nguyên tố vì nó chia hết cho (1 2 4 và 8)
Gợi ý: sử dụng biến count (vì số nguyên tố chỉ chia hết cho 2 số nên count = 2, 
số không phải nguyên tố chia hết cho nhiều hơn 2 số)
count = 0
a = int(input()) # a = 13
# kiểm tra xem các số từ 1 đến 13 thì 13 chia hết cho những số nào
# Nếu nó chỉ chia hết cho 1 và 13 -> tăng biến count lên 1 và không chia hết cho các số khác thì nó là nguyên tố
# Nghĩa là đếm được count = 2 thì ra kiểm tra if else
for i in range(1,a+1):
    if a % i == 0 :
        count += 1
# count = 2 là số nguyên tố, trường hợp còn lại k phải nguyên tố
# if else phải dùng 2 dấu bằng để so sánh, đừng quên điều kiện 2 dấu bằng, 1 = là sai cú pháp
if count == 2:
    print("là số nguyên tô ")
else:
    print("không phải số nguyên tố")
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
for i in range(1,11):
    if i != 3 and i != 8:
        print(i)
# Continue: bỏ qua giá trị:
for i in range(1,11):
    if i == 3 or i == 8:
        continue
    print(i, end=" ")
print()
# In ra các số chẵn (nghĩa là bỏ qua các số lẻ) từ 1 đến 10 sử dụng continue
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i,end=" ")
# break: thoát vòng lặp:
# In ra số đầu tiên chia hết cho 3 trong đoạn từ 1 đến 30
for i in range(1,31,1):
    if i % 3 == 0:
        print(i, end=" ")
        break
"""

# In ra 3 số đầu tiên chia hết cho 3 và 5 trong đoạn từ 1 đến 200:
# Gợi ý: dùng count, for và break
count = 0
for i in range(1,201):
    if i % 3==0 and i % 5 == 0:
        print(i,end=" ")
        count+= 1
    if count == 3:
        break