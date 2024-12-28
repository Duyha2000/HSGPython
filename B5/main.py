# continue: bỏ qua giá trị/điều kiện - break: dừng lại giá trị
# Vòng lặp for

# vòng lặp while:

# In ra casc số từ 1 -> 5
"""
for i in range(1,6):
    print(i, end=" ")
"""
# Vòng lặp while:

"""
while: lặp khi 

while condition:
    # code
    # step: bước nhảy
"""
"""
i = 1
while i <=5:
    # code
    print(i, end=" ") # 1 2 3 4 5
    # Thoát vòng lặp khi i > 5
    # Step:
    i+=1
"""
# Nhập 2 số a , b -> in ra các số chẵn trong đoạn [a,b]
# Ví dụ: a = 1 -> b = 10
# In ra 2 4 6 8 10

"""
print()
a = int(input()) # a = 1
b = int(input()) # b = 10

for i in range(a,b+1):
    if i % 2 == 0:
        print(i, end=" ")
while a<=b:
    if a % 2 ==0:
        print(a, end=" ")
    # Step:
    a+=1
"""
# Bài tập 9: In ra số dương nhỏ nhất chia hết cho 3 5 và 7:
# ? ko thể biết được số dương nào thỏa mãn
# số dương nhỏ nhất là số 1

# for i in range(1,end+1): -> ko dùng vòng for ược vì không biết nó kết thúc khi nào

n = 1
# cho n = 1 -> tăng dần giá trị này -> đến khi bắt gặp số chia hết cho 3 5 7 thì in ra và thoát vòng lặp
while True:
    if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
        print(n, end=" ")
        break

    # step:
    n+=1
# In ra 3 số dương chia hết cho 3 và 8
