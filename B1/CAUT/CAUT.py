file_input=open("CAUT.INP","r")
file_output=open("CAUT.OUT","w")
output=""
count = 0
for i in range(2):
    n = int(file_input,readline())
        if n % j == 0:
         count +=1
    if count == 2:
        output += "1/n"
    else:
        output +="0/n"
    