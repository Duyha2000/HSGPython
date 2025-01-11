file_input=open("RUTGON.INP","r")

file_output=open("RUTGON.OUT","w")
output=" "
for i in range(1):
    a, b = map(int,file_input.readline().split())
    """
    for j in range (1,a+1):
         if a % j ==0 :
            output+=str(j) + " "
    output += "\n"
    for l in range(1,b+1):
         if b % l == 0 :
            output+=str(l) +" "
    """
    uocChungLonNhat = 1 # 6
    for n in range(1, a + 1):
        if a%n == 0 and b %n == 0:
            uocChungLonNhat = n
    # Rút gọn a,b:
    output += str(a // uocChungLonNhat) + " " # 2
    output += str( b // uocChungLonNhat) # 3

file_output.write(output)