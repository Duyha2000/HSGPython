"""
Cho một list các số nguyên n phần tử lst được nhập từ bàn phím.
Bài 1: Viết chương trình Python tính tổng các phần tử của danh sách
Bài 2: Viết chương trình Python đếm số lượng các số hạng dương và tổng của các số hạng dương.
Bài 3: Viết chương trình Python tính trung bình cộng của cả danh sách, trung bình cộng các phần tử dương trong danh sách.
Bài 4: Viết chương trình Python tìm vị trí của phần tử âm đầu tiên trong danh sách.
Bài 5: Viết chương trình Python tìm vị trí của phần tử dương cuối cùng trong danh sách.
Bài 6: Viết chương trình Python tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
Bài 7: Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử đạt giá trị lớn nhì.
lst=[1,2,3,4,5]
sum=0
for number in lst :
    sum+=number
print(sum)
lst=[1,2,3,4,-5]
sum=0
count=0
for number in lst:
    if number > 0:
       count += 1
       sum += number
print(count)
print(sum)
lst=[1,2,3,4,-5]
sum=0
count=0
for number in lst:
    if number >0:
        count+=1
        sum+=number
TBC=sum/count
print(TBC)
position = -1
lst=[1,2,3,4,-5]
for i in lst:
    if i < 0:
        position = lst.index(i)
        break # break là phần tử đầu tiên
5
print(position)
lst=[-1,-2,3,4,-5]
position = -1
for i in lst :
    if i > 0:
        position = lst.index(i)
print(position ) # 3
# https://docs.google.com/document/d/1h7Cvt9ILkPJwZCCObQE8QFSqnejyJ2b3WzRZ8Ewoh_c/edit?tab=t.0
#Bài 1 :
lst = [1,2,3,4,5]
sum = 0
for number in lst:
    sum+=number
print(sum)
#Bài 2 :
#a)
lst = [3,4,5,4,5]
print(max(lst))
print(min(lst))
#b)
lst = [2, 9, 6, 6, 7, 8]
lst.sort()
print(lst)
Bài 3 :
lst = [2, 9, 8, 7, 9]
lst.reverse()
print(lst)
#Bài 4:
lst = [ 3 ,1 ,2 ,5 ,4 ,4 ,5 ]
postion = -1
for i in lst :
    if i < max(lst):
        postion = lst.index(i)
print(postion)
"""
# Bài 5:

