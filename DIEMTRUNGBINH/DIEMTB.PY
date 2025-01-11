file_input=open("DIEMTB.INP","r")
file_output=open("DIEMTB.OUT","w")
output= ""
for i in range (2):
    X, Y = map(int, file_input.readline().split())
    DTB = (X * 3 + Y) / 4
    if DTB >=5:
        output += "1\n"
    else:
        output += "0\n"
file_output.write(output)