file_input=open("CAU1.INP", "r")
file_output=open("CAU1.OUT","w")
output= ""
for i in range(2):
    n = int(file_input.readline())
    count = 0
    for j in range(1, n+1):
        if n % j == 0:
            count +=1
    if  count == 2:
        output+="1 \n"
    else :
        output+="0 \n"
file_output.write(output)

# Giả sử input có 2 dòng: for i in range(2)
# Nếu 1 dòng có nhiều dữ liệu (ví dụ 3 dữ liệu) a,b,c = map(int, file_input.readline().split())
# Ví dụ chỉ có 1 dữ liệu: n = int(file_input().readline())