file_input = open("RUTGONSO.INP","r")
file_output = open("RUTGONSO.OUT","w")
output = ""

for i in range(1):
    a, b = map(int,file_input.readline().split())
    # In ra các ước của a:
    # In ra các ước của b
    # Vòng for:
    # for j in range():
    #     if a % j == 0 and b % j == 0:
    #         output = str()
    """
    for j in range(1,a+1):
        if a % j == 0:
           output += str(j) +""
    output += "\n"
    for l in range(1,b+1):
        if b % l == 0:
            output += str(l) +""
    """
    for n in range(1,a+1):
        if a % n == 0 and b % n == 0:
           uocchunglonnhat = n
    # Rút gọn a,b
    output += str(a // uocchunglonnhat) +" "
    output += str(b // uocchunglonnhat) +" "
file_output.write(output)
