# File để code:
# Mở 2 file input và output:
file_input = open("UOC.INP","r")
file_output = open("UOC.OUT","w")
output = ""

count = 0
N = int(file_input.readline()) # 12

for i in range(1,N+1):
    if N % i == 0:
        count += 1

output = str(count)

# Ghi dữ liệu vào file output:
file_output.write(output)