file_input=open("CHUVI.INP","r")
file_output=open("CHUVI.OUT","w")
output=""
for i in range(2) :
    a,b,c = map(int,file_input.readline().split())
    CHUVI=a+b+c
    output += str(CHUVI) + "\n"


file_output.write(output)
