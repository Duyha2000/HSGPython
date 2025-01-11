file_input = open("SOHOC.INP","r")
file_output = open("SOHOC.OUT","w")
output = ""

for i in range(1):
    n = int(file_input.readline())
    count = 0
    for j in range(1,n+1):
        if n % j == 0:
           count += 1
    if count == 3:
        output += "1\n"
    else:
        output += "0\n"
    output = str(output)

file_output.write(output)