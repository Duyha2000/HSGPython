# File để code:
# Tính tổng các số từ 1 đến N:
# Xử lý file input và file Output:
# Mở 2 file input và output:
file_input = open("SUM.INP","r") # read
file_output = open("SUM.OUT","w") # write
output = ""

N = int(file_input.readline())

sum = 0
for i in range(1,N+1):
    sum = sum + i
# Thực hiện logic và in kết quả dưới terminal
output = str(sum)

# Ghi kết quả vào file SUM.output
file_output.write(output)
