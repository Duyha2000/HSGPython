file_input=open("DIEMTB.INP","r")
file_output=open("DIEMTB.OUT","w")
output=""

for i in range(2):
    x, y = map(int, file_input.readline().split())
    DTB = (x * 3 + y) / 4
    if DTB >= 5:
        output +="1\n"
    else:
        output +="0\n"

file_output.write(output)