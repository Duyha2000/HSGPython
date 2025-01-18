# https://whimsical.com/danh-sach-5RbC42aQmZhjSWeQXukBi6
# Danh sách (list): lưu trữ nhiều dữ liệu khác nhau:
#  = []
lst = ["Ly","Thanh","Hung","Dung","Thuy"]

# Chỉ số: bắt đầu từ 0:
print(lst[1]) # "Thanh"

# Chỉ số cối cùng danh sách: -1
print(lst[-1])

# Duệt qua danh sach: for - in:
for i in lst:
    print(i,end=" ")
# tính toán, sử dụng để in ra các thông tin, đêm
# len(): length: đếm xem có bao nhiêu phần tử trong danh sách
# min, max
print(len(lst))
# sort(): sắp xếp tăng dần
# reverse() : đảo ngược danh sách
lstNumber = [1,3,5,7,8]
# THêm 1 số vào danh sách:

# append: thêm 1 phần tử vào cuối danh sách:
lstNumber.append(6)
print(lstNumber) # [1, 3, 5, 7, 8, 6]
#                   0  1  2  3  4  5

# insert: thêm 1 phần tử vào chỉ số mong muốn:
lstNumber.insert(3,6) # [1, 3, 5, 6, 7, 8, 6]
print(lstNumber)

"""
Bài Tập 6: Chèn một phần tử vào mảng
Mô tả: Yêu cầu người dùng "nhập" một mảng các số nguyên, "một vị trí" và "một số". Chèn số vào mảng tại vị trí đã chỉ định. Nếu vị trí không hợp lệ, in ra lỗi.
Ví dụ Đầu Vào: arr = [3, 5, 6, 7], position = 2, number = 5
Ví dụ Đầu Ra: [3, 5, 5, 6, 7]
"""
"""
index = int(input("Nhap vi tri:"))
number = int(input("Nhap vi tri:"))

lstNambo= [3,5,6,7]
lstNambo.insert(index,number)
print(lstNambo)
vowels = [3,5,6,7]
index = int(input("Nhap vi tri:"))
number = int(input("Nhap số:"))
vowels.insert(index,number)
print(vowels) # [3, 5, 5, 6, 7]
"""
# Xóa phần tử trong danh sách: remove, pop

# Remove: xóa phần tử cho trước:
"""
vowels = [3,5,6,7]
# Xóa đi số 6:
vowels.remove(6)
print(vowels) # [3, 5, 7]
"""
"""
vowels = [1,2,3,4,5]
vowels.remove(1)
print(vowels) # [2, 3, 4, 5]

# pop(): xoa một phần tử tại 1 chỉ số, nếu không viết gì thì sẽ xóa đi phần tử cuôi:
vowels.pop()
print(vowels) # 2 [3] 4
vowels.pop(1)
print(vowels) # 2 4

lst = [1,2,3,4,5]
lst.pop(1)
print(lst)
lst.pop()
print(lst)
"""
lst = [1,2,3,4,5]
#      0 1 2 3 4
# Cập nhật phần tử: chuyển số 3 -> 9
lst[2] = 9
print(lst) # [1, 2, 9, 4, 5]


# Cho 1 danh sách 5 phần tử, trả về "vị trí" (chỉ số) phần tử dương đầu tiên trong danh sách. Nếu không
# tìm thây trả về -1
# lst = [-2,-4,5,6,-7 ]
# Output: 2 (chỉ số)

# lst = [-2,-4,-6,-2,-9]
# Output: -1
position = -1 # "chi so, vi tri"
lst = [-2,-4,6,-2,-9]
#            ->
for i in lst:
    if i > 0:
        position = lst.index(i) # lst.index(i): trả về chỉ số phần tử thỏa mãn
        break # break để không chạy các phần tử tiếp theo (vì chỉ cần chỉ số đâu tiên)
print(position) # -1
