"""
Cho một list các số nguyên n phần tử lst được nhập từ bàn phím.
Bài 1: Viết chương trình Python tính tổng các phần tử của danh sách
Bài 2: Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
Bài 3: Viết chương trình Python tính trung bình cộng của cả danh sách,
trung bình cộng các phần tử dương trong danh sách.
Bài 6: Viết chương trình Python tìm phần tử lớn nhất của danh sách.
Bài 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách.
"""
"""
#bài 1
tong = 0
lst = [1,-2,3,-4,6,-5,9]
for number in lst:
    if number > 0:
       tong += number
print(tong)

# bài 2
count = 0
sum = 0
for number in lst:
    if number > 0:
        count += 1
        sum += number
print(sum)
# bài 3
sum = 0
sumDuong = 0
count = 0
lst = [1,-2,3,-4,5,-6,7,-8,9,10]
for number in lst:
    sum +=number
    if number > 0:
       sumDuong += number
       count += 1
print(sum/len(lst))
print(sumDuong/ count)

#bài 6

lst = [1,-2,3,9,-4,6,9,-5]
print(max(lst))
"""
# In ra số 6
# B1: Sắp xếp danh sách tăng dần
# B2: Dùng for để so sánh max và các số khác, số nào < max -> in ra số đấy rồi break
lst = [1,-2,6,9,-4,9,-5]
lst.sort()
print(lst)
solonthuhai = lst[0]
for number in lst:
    if number < max(lst):
        solonthuhai = number
print(solonthuhai)
"""
Bài Tập 5: Đếm số lần xuất hiện của một giá trị trong mảng
Mô tả: Yêu cầu người dùng nhập một mảng các số nguyên và một giá trị mục tiêu. 
Sau đó, tìm và in ra số lần giá trị mục tiêu xuất hiện trong mảng.
Ví dụ Đầu Vào: arr = 3 4 5 3, X = 3
Ví dụ Đầu Ra: 2
Gợi ý: count = 0 -> nếu thỏa mãn điều kiện: count+=1

"""
count = 0
lst =[3,4,5,3]
x = 3
for number in lst:
    if x == number:
        count += 1
print(count)