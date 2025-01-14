# https://whimsical.com/danh-sach-5RbC42aQmZhjSWeQXukBi6
# Danh sách: list - array: lưu trữ nhiều dữ liệu khác nhau
#  []: khai báo 1 danh sách
# Lưu số: 1 2 3 4 5
a = 1
b = 2
c = 3
d = 4
e = 5

lst = [-1,2,-3,4,-5,9,-8,6] # Danh sách các số nguyên
lstName = ["Thúy","Lý","Thanh","Minh"] # Danh sách tên

# Chỉ số của danh sách (index): Bắt đầu từ 0

# Danh sách số nguyên:                                            1 2 3 4 5 9 7 5
#  Chỉ số: để lấy giá trị số hoặc chữ trong danh sách        ->   0 1 2 3 4 5 6 7

# Lấy được 1 số trong danh sách: cú pháp:  lst[index]
print(lst[3]) # 4
print(lstName[1]) # Lý
# Lấy ra được chiều dài của danh sách (số phần tử): len(lst)
print(len(lst)) # 8
# Max , min

print(max(lst)) # 9
print(min(lst)) # 1

# Lấy phần tử cuối cùng trong danh sách (không cần đếm bằng mắt):
# Lấy ra số 6
print(lst[0]) # 1
print(lst[-1]) # index = -1 lấy ra phần tử cuối trong danh sách
print(lstName[-1])
# Sort: sắp xếp (tăng / giảm ) dần:
lst.sort()
print(lst) # [1, 2, 3, 4, 5, 6, 8, 9]
# Reverse: đảo ngược các phần tử:
lst.reverse()
print(lst) # [9, 8, 6, 5, 4, 3, 2, 1]

# Danh sách lstName: sort - reverse
lstName.sort()
print(lstName)
lstName.reverse()
print(lstName)

# Lặp qua các phần tử trong danh sách (tổng, tích, đếm số) trong danh sách
# Tính tổng các số trong danh sách:
#print(lst[0] + lst[1] + lst[2] + ... + lst[-1])

# for - in: nằm trong: lấy ra các phần tử (số / chuỗi) trong danh sách
for number in lst:
    if number > 0:
        pass
        # print(number, end=" ")
# In ra các s
# số chẵn trong danh sách lst:
for number in lst:
    if number % 2 == 0:
        pass
        # print(number,end=" ")
# Đếm các số > 0 và là số chẵn trong danh sách lst:
count = 0
for number in lst :
    if number > 0 and number % 2 == 0:
        count+=1
print(count)
"""
Cho một list các số nguyên n phần tử lst được nhập từ bàn phím.
Bài 1: Viết chương trình Python tính tổng các phần tử của danh sách
Bài 2: Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
Bài 3: Viết chương trình Python tính trung bình cộng của cả danh sách, trung bình cộng các phần tử dương trong danh sách.
Bài 4: Viết chương trình Python tìm vị trí của phần tử âm đầu tiên trong danh sách.
Bài 5: Viết chương trình Python tìm vị trí của phần tử dương cuối cùng trong danh sách.
Bài 6: Viết chương trình Python tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
Bài 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử đạt giá trị lớn nhì.
"""