# Open:
file_input = open("TAMGIAC.INP","r")
file_output = open("TAMGIAC.OUT","w")
output = ""

# Vòng for thể hiện cho số lần lặp:
for i in range(4):
    a,b,c = map(int, file_input.readline().split())
    if a + b + c <180 or a <= 0 or b <=0 or c <=0:
        output +="0 \n"
    elif a < 90 and b < 90 and c <90:
        output +="NHON \n"
    elif a == 90 or b == 90 or c ==90:
        output += "VUONG \n"
    else:
        output +="TU \n"

# Viet file:
file_output.write(output)