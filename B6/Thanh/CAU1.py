file_input = open("CAU1.INP","r")
file_output = open("CAU1.OUT","w")
output = ""

for i in range(2):
    sum = 0
    n = int(file_input.readline()) # n = 3
    for j in range(2, n+1):
        sum += (j - 1) * j * (j + 1)
    output += str(sum) +"\n"


file_output.write(output)