"""
Cho một list các số nguyên n phần tử lst được nhập từ bàn phím.
Bài 1: Viết chương trình Python tính tổng các phần tử của danh sách
Bài 2: Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
Bài 3: Viết chương trình Python tính trung bình cộng của cả danh sách, trung bình cộng các phần
 tử dương trong danh sách.
Bài 4: Viết chương trình Python tìm vị trí của phần tử âm đầu tiên trong danh sách.
Bài 5: Viết chương trình Python tìm vị trí của phần tử dương cuối cùng trong danh sách.
Bài 6: Viết chương trình Python tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất
cuối cùng.
Bài 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các
phần tử đạt giá trị lớn nhì.
#bài 1
sum = 0
lst = [1,-2,3,-4,6,-5,9]
for number in lst:
    if number > 0:
        sum += number

print(sum)
#bài 2
count = 0
sum =0
lst = [1,-2,3,-4,6,-5,9]
for number in lst:
    if number > 0:
        count += 1
        sum += number
print(sum)
print(count)

#bài 3
sum = 0
sumduong = 0
count = 0
lst = [1,-2,3,-4,6,-5,9]
for number in lst:
    sum += number
    if number > 0:
        sumduong += number
        count += 1
print(sum/len(lst))
print(sumduong/count)
#bài 4
lst = [-1,-2,3,-4,6,-5,9]
position = -1

for i in lst:
    if i > 0:
        position = lst.index(i)
        break # break là phần tử đầu
print(position)

#bài5
lst = [-1,-2,3,-4,6,-5,9]
position = -1

for i in lst:
    if i > 0:
        position = lst.index(i)

print(position)
#bài 6
lst = []
print(max(lst))
print(lst.index(max(lst))) # vị trí phần tử lớn nhất cuối cùng:
#bài 7
lst = [-1,-2,3,-4,6,-5,9]
lst.sort()
print(lst)
solonthuhai = lst[0]
for number in lst:
    if number < max(lst):
       solonthuhai = number
print(solonthuhai)
print(lst.index(solonthuhai))
"""
# https://docs.google.com/document/d/1h7Cvt9ILkPJwZCCObQE8QFSqnejyJ2b3WzRZ8Ewoh_c/edit?t
#ab=t.0
#bài 1
sum= 0
lst = [ 1, 2, 13, 30, 45]
for number in lst:
    if number % 3 == 0 and number % 5 == 0:
        sum += number
print(sum)

#bài 2a
lst = [ 3, 4,5,4,5 ]
print(max(lst))
print(min(lst))

#bài 2b
lst = [2,9,6,6,7,8]
lst.sort() # sắp xếp tăng dần:
print(lst)
lst.reverse() # [9, 8, 7, 6, 6, 2]
print(lst) # [2, 6, 6, 7, 8, 9]

#bài 3
lst = [2,9,8,7,9,0,1,2,3,4]
lst.reverse()
print(lst)

#bài 4
lst = [1,2,3,4,4,5,5]
lst.sort()
print(lst)
solonthuhai = lst[0]
for number in lst:
    if number < max(lst):
        solonthuhai = number
print(solonthuhai)

#bài 5
count = 0
lst = [3,4,5,3]
x = 3
for number in lst:
    if x == number:
        count += 1
print(count)

#bài 9
lst = [2,9,6,6,7,8]
lst.sort()
print(lst)

#bài 6
vowels = [3,5,6,7]
vowels.insert(2,5)
print(vowels)

#bài 8
# Phần 1:
lst = [4,6,7,8]
lst.pop(2)
print(lst)
# Phần 2:
lst2 = [5,6,7,6,6,9]
lst3 = []
number = 6
for i in lst2:
    if number != i:
        lst3.append(i)

# Vòng lặp for:
## lst2.remove(number)
print(lst3)