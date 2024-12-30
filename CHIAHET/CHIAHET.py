file_input=open("CHIAHET.INP","r")
file_output=open("CHIAHET.OUT","w")
output = ""
# Lấy số 2 và số 3 trên cùng 1 dòng từ file SPOW.INP
A,B = map(int, file_input.readline().split())
for i in range(A,B+1) :
    if i % 3 == 0 and i % 5 == 0:
        output += str(i) +"\n"
file_output.write(output)