# Mở file input và output:
file_input = open("SPOW.INP","r")
file_output = open("SPOW.OUT","w")
output = ""
# Lấy số 2 và số 3 trên cùng 1 dòng từ file SPOW.INP
a,n = map(int, file_input.readline().split())
# a,n là int -> out là kiểu string
# Cần phải eutput += str(a + n) +"\n" ́p kiểu dữ liệu:
o# \n để xuống dòng

output += str(a**n) # "8"

# Ghi kết quả vào file:
file_output.write(output)