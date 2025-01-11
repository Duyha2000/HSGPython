file_input=open("BERTRAN.INPUT","r")
file_output=open("BERTRAN.OUT","w")
output=""
for i in range(2):
    p = int(file_input,readline())
    count = 0
    # Vòng for kiểm tra nguyên tố
    for i in range(1,):
        if p % i ==0:
            count += 1
    if count == 2:
        output += str(count)+"3\n"
    else:
        output += str(count)+"5 7 \n"
file_output.write(output)
